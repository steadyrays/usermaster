import numpy as np
import pandas as pd

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Page, Pie ,HeatMap


def data_clean(data):
    '''数据预处理'''

    '''时间类型修改'''
    data['订单日期'] = pd.to_datetime(data['订单日期'], format="%m/%d/%Y %H:%M")  #

    '''添加订单月份'''
    data['订单月份'] = data['订单日期'].values.astype('datetime64[M]')

    '''添加订单金额'''
    data['订单金额'] = data['数量'] * data['单价']

    '''删除缺失值'''
    data.dropna(inplace=True)

    '''删除重复数据'''
    data.drop_duplicates(inplace=True)

    '''去除数量为负数的数据'''
    data = data[data['数量'] > 0]  #
    return data

def line_of_sale(data):
    data=data.groupby('订单月份')['订单金额'].sum()
    data.index=data.index.astype(np.str)
    c = (
        Line()
            .add_xaxis(data.index.tolist())
            .add_yaxis("总业绩",data.values.tolist(),is_smooth=True,color=Faker.rand_color())
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
            .set_global_opts(title_opts=opts.TitleOpts(title="每日销售总业绩(元)"))
    )
    return c

def line_of_pareto(data):
    gp_user = data.groupby("用户id")['订单金额'].sum().reset_index().sort_values("订单金额")
    gp_user['订单累计'] = gp_user['订单金额'].cumsum()
    gp_user['prob'] = gp_user['订单累计'] / (gp_user['订单金额'].sum())
    c = (
        Line()
            .add_xaxis(list(range(len(gp_user))))
            .add_yaxis("用户消费业绩占比", gp_user['prob'].values.tolist(),color=Faker.rand_color())
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
            .set_global_opts(title_opts=opts.TitleOpts(title="每日销售总业绩(元)"))
    )
    return c

def line_of_fgl(data):
    data['订单月份'] = data['订单月份'].astype(np.str)
    fgl_pvt = pd.pivot_table(data=data, index='用户id', columns='订单月份', values='订单编号', aggfunc='count')
    # 这里添加一个判断条件及复购率的次数要求
    fgl_pvt = fgl_pvt.applymap(lambda x: np.nan if np.isnan(x) else 1 if x >= 10 else 0)
    fgl = fgl_pvt.mean()
    x=fgl.index.tolist()
    y=fgl.values.tolist()
    c = (
        Line()
            .add_xaxis(x)
            .add_yaxis("复购率",y,color=Faker.rand_color(),is_smooth=True)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             )
            .set_global_opts(title_opts=opts.TitleOpts(title="每月复购率波动图"),
                             yaxis_opts=opts.AxisOpts(is_scale=True))# 设置轴刻度自适应
    )
    return c

def bar_of_io(data):
    user_in=data.groupby("用户id")['订单月份'].min().value_counts().reset_index()
    user_in.columns=['订单月份','流入客户人数']
    user_out=data.groupby("用户id")['订单月份'].max().value_counts().reset_index()
    user_out.columns=['订单月份','流出客户人数']
    user_all=pd.merge(user_in,user_out).sort_values("订单月份")
    x=user_all['订单月份'].tolist()
    y1=user_all['流入客户人数'].tolist()# 用户首次消费的时间
    y2=user_all['流出客户人数'].tolist()# 用户停止消费的时间

    c = (
        Bar()
            .add_xaxis(x)
            .add_yaxis("流入客户人数",y1)
            .add_yaxis("流出客户人数",y2)
            .set_global_opts(title_opts=opts.TitleOpts(title="客户每月的留存情况预览"))
    )
    return c

'''用户分层模型适合用堆积柱状图展示'''
def bar_of_fc(data):
    def fc_func(data):
        result = []
        for i in range(len(data)):
            if np.isnan(data.iloc[i]):
                result.append(np.nan)
            else:  # 如果当月消费了,同时result里面没有统计到新用户
                if result.count('新用户') == 0:
                    result.append('新用户')
                else:
                    if not np.isnan(data.iloc[i - 1]):  # 上个月是否消费
                        result.append('活跃用户')
                    elif np.isnan(data.iloc[i - 1]) and np.isnan(data.iloc[i - 2]):
                        result.append('回流用户')
                    else:
                        result.append('不活跃用户')
        return pd.Series(result, index=data.index.astype(np.str))

    pivoted_fc=data.pivot_table(index='用户id', columns='订单月份', values='订单编号', aggfunc='count')
    user_fc = pivoted_fc.apply(fc_func, axis=1)
    fc_plot = user_fc.apply(lambda x: x.value_counts())
    fc_plot = fc_plot.fillna(0).T.sort_index()
    c = (
        Bar()
        .add_xaxis(fc_plot.index.tolist())
        .add_yaxis("新用户",fc_plot['新用户'].tolist(), stack="stack1")
        .add_yaxis("活跃用户",fc_plot['活跃用户'].tolist(),stack="stack1")
        .add_yaxis("不活跃用户",fc_plot['不活跃用户'].tolist(),stack="stack1")
        .add_yaxis("回流用户",fc_plot['回流用户'].tolist(),stack="stack1")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="消费用户分层"))
    )
    return c

def heatmap_of_retention01(data):
    first_purchase = data.groupby("用户id")['订单月份'].min().reset_index()
    first_purchase.columns = ['用户id', '首单月']
    sales_retention = pd.merge(data, first_purchase).groupby(["订单月份", "用户id"]).head(1)
    retention = sales_retention.pivot_table(index='订单月份', columns='首单月', values='用户id', aggfunc='count')
    retention.columns = retention.columns.astype(np.str)
    retention.index = retention.index.astype(np.str)
    lc = retention / retention.max()
    value = [[i, j, lc.iloc[i, j] * 100] for i in range(len(lc.index)) for j in range(len(lc.columns))]

    c = (
        HeatMap()
            .add_xaxis(list(lc.index))  # x轴
            .add_yaxis("用户留存分析图", list(lc.columns), value)  # y轴和值
            .set_global_opts(
            title_opts=opts.TitleOpts(title="每月用户留存情况"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c

def heatmap_of_retention02(data):
    first_purchase = data.groupby("用户id")['订单月份'].min().reset_index()
    first_purchase.columns = ['用户id', '首单月']
    sales_retention = pd.merge(data, first_purchase).groupby(["订单月份", "用户id"]).head(1)
    def f(data):
        diff = data['订单日期'] - data['订单日期'].min()
        data['消费间隔月'] = diff.map(lambda x: x.days // 30 + 1)
        return data
    sales_retention = sales_retention.groupby('用户id').apply(f)
    retention = sales_retention.pivot_table(index='消费间隔月', columns='首单月', values='用户id', aggfunc='count')
    retention.index = retention.index.map(lambda x: "第%s月" % x)
    retention.columns = retention.columns.astype(np.str)
    lc = retention / retention.max()
    value = [[i, j, lc.iloc[i, j] * 100] for i in range(len(lc.index)) for j in range(len(lc.columns))]

    c = (
        HeatMap()
            .add_xaxis(list(lc.index))  # x轴
            .add_yaxis("用户留存分析图", list(lc.columns), value)  # y轴和值
            .set_global_opts(
            title_opts=opts.TitleOpts(title="每月用户留存情况"),
            visualmap_opts=opts.VisualMapOpts(),
        )
    )
    return c

# def heatmap_of_retention03(data):
#     first_purchase = data.groupby("用户id")['订单月份'].min().reset_index()
#     first_purchase.columns = ['用户id', '首单月']
#     sales_retention = pd.merge(data, first_purchase).groupby(["订单月份", "用户id"]).head(1)
#     def f(data):
#         diff = data['订单日期'] - data['订单日期'].min()
#         data['消费间隔月'] = diff.map(lambda x: x.days // 30 + 1)
#         return data
#     sales_retention = sales_retention.groupby('用户id').apply(f)
#     retention = sales_retention.pivot_table(index="消费间隔月", columns="国家", values='用户id', aggfunc='count')
#     retention.index = retention.index.map(lambda x: "第%s月" % x)
#     retention.columns = retention.columns.astype(np.str)
#     lc = retention / retention.max()
#     new_index = lc.count().sort_values(ascending=False).index
#     lc = lc.reindex(columns=new_index)
#     value = [[i, j, lc.iloc[i, j] * 100] for i in range(len(lc.index)) for j in range(len(lc.columns))]
#
#     c = (
#         HeatMap()
#             .add_xaxis(list(lc.index))  # x轴
#             .add_yaxis("用户留存分析图", list(lc.columns), value)  # y轴和值
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="不同国家的用户留存情况"),
#             visualmap_opts=opts.VisualMapOpts(),
#         )
#     )
#     return c

'''读取数据'''
f = open(r"电子商务数据集1.csv", encoding='utf-8', errors='ignore')
sales = pd.read_csv(f)
f.close()

'''
invoiceNo 发票号码 Description 货物描述 InvoiceDate发票日期 CustomerID 客户账号
stockCode 货物代码 Quantity 数量 UnitePrice 单价 Country 客户所在国家
'''
sales.head()

'''重新设置列名'''
columns=['订单编号','货物代码','货物描述','数量','订单日期','单价','用户id','国家']
sales.columns=columns

sales=data_clean(sales)

page = Page(layout=Page.SimplePageLayout)

'''添加每月销售折线图'''
page.add(line_of_sale(sales))

'''添加帕累托图'''
page.add(line_of_pareto(sales))

'''添加复购率'''
page.add(line_of_fgl(sales))

'''客户的流入与流出'''
page.add(bar_of_io(sales))

'''客户分层'''
page.add(bar_of_fc(sales))

'''用户留存'''
page.add(heatmap_of_retention01(sales))
page.add(heatmap_of_retention02(sales))
# page.add(heatmap_of_retention03(sales))

page.render()

'''时间数据展示'''
