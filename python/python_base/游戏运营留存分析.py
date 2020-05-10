import numpy as np
import pandas as pd
import time

def time_add(start_time,ndays):
    st_sec=time.mktime(time.strptime(start_time,"%Y-%m-%d"))
    et_sec=st_sec+ndays*24*60*60
    et=time.strftime("%Y-%m-%d",time.localtime(et_sec))
    return et

# 统计某天登录的用户经过xx天的点留存
def dlc(date,days):
    all_user=df.query('日期==@date')['uid'].unique()
    diff_days=time_add(date,days)
    # print(diff_days)
    daydiff_30=df.query('日期==@diff_days')['uid'].unique()
    lc=np.isin(daydiff_30,all_user).sum()/len(all_user)# 5日点留存
    return round(lc,4)

# 统计某天登录的用户经过xx天内的区间留存
def qjlc(date,days):
    all_user=df.query('日期==@date')['uid'].unique()
    qjst=time_add(date,1)
    qjdt=time_add(date,days)
    qjlc_5=df.query('@qjst<=日期<=@qjdt')['uid'].unique()
    lc=np.isin(qjlc_5,all_user).sum()/len(all_user)
    return round(lc,4)

# 根据需求产生留存分析表
def get_lc(time_list,dlc_list,qjlc_list):
    # time_list需要统计的时间
    # dlc_list点留存参数
    # qjlc_list区间留存参数
    d1={'第%s天后的点留存'%i:{t:dlc(t,i) for t in time_list} for i in dlc_list}
    d2={'第%s天后的区间留存'%i:{t:dlc(t,i) for t in time_list} for i in qjlc_list}
    d1.update(d2)# 讲区间留存和点留存的字典合并
    return pd.DataFrame(d1)


path = r'C:\Users\ibf\Documents\Tencent Files\3004438828\FileRecv\留存分析 (1).xlsx'
df = pd.read_excel(path)
def main():# 定义主函数
    result=get_lc(['2012-11-06','2012-11-07','2012-11-08'],[1,3,5],[1,3,5])
    result.index='日期'
    result.to_csv("留存分析表.csv")

main()