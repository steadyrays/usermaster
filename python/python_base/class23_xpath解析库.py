# xpath
from lxml import etree

text='''
    <html>
        <head>
            <title>春晚</title>
        </head>
        <body>
            <h1 name="title">个人简介</h1>
            <div name="desc1">
                <p name="first" id="123">姓名：<span>小岳岳</span></p>
                <p name = "second" class="abc">住址1：中国 河南</p>
                <p name="third"></p>
            </div>
            <div name="desc2">
                <p name = "第一" id="123">姓名：<span>小岳岳</span></p>
                <p name = "第二" class="ABC">住址2：中国 河南</p>
                <p name = "第三">代表作：五环之歌</p>
            </div>
'''

# 初始化
html=etree.HTML(text)
# print(html)

# 通过全路径查询标签(绝对路径、相对路径)
# all_p=html.xpath('ml/body/div/p')# 返回列表,参数是路径
# print(all_p)
# all_p=html.xpath('ml/body/div[@name="desc1"]/p')
# print(all_p)
'ml/body/div[1]/div/div[2]/ul[1]/a'

# 产看标签属性
# 文本信息
# print(all_p[0].text)# 查看标签的文本属性
# 提取多个标签中的信息
# for p in all_p:
#     print('循环打印标签文本信息:',p.text)
# all_text=html.xpath('ml/body/div/p/text()')# 返回列表
# print("提取标签中对应的所有文本信息:",all_text)

# 标签文本为空时,提取不到任何结果

# 获取多个标签中的其他属性
# all_name=html.xpath('ml/body/div/p/@name')# @属性名
# print("提取标签中对应的所有name属性:",all_name)
# all_class=html.xpath('ml/body/div/p/@class')# @属性名
# print("提取标签中对应的所有class属性:",all_class)

# 其他的查询标签方法
# print(html.xpath('//p'))# 查询所有的p标签
# print(html.xpath('//p/text()'))# 查询所有的p标签
# print(html.xpath('//div'))# 查询所有的div标签
# print(html.xpath('//div/text()'))# 查询所有的div标签
# print(html.xpath('//@id'))# 查询所有的id属性
# print(html.xpath('//@name'))# 查询所有的name属性

# 结合属性进行标签定位
# print(html.xpath('//p[@name="first"]/text()'))

# 针对标签提取标签下的所有信息
p=html.xpath('//p[@name="first"]')[0]
# print(p.xpath('string(.)'))# 获取标签下所有字符信息

# 获取第二个div下的所有信息
# div1=html.xpath('ml/body/div[2]')
# div2=html.xpath('//div[@name="desc2"]')
# print(div1,div2)
# print(div1[0].xpath('string(.)'))
# print(div2[0].xpath('string(.)'))

# p=html.xpath('//p[@name="third"]')[0]
# s=p.xpath('string(.)')# 对于标签内容为空的结果范围空字符串
# print(s,len(s),type(s))

# 获取第一个和最后一个标签
# p_x=html.xpath('//p[last()]/text()')
# print(p_x)
# p_x=html.xpath('//div[@name="desc2"]/p[last()-1]/text()')
# print(p_x)

# 构建多个标签对象
# print(html.xpath('ml/body/div[2]/p'))
# div=html.xpath('ml/body/div[2]')[0]
# print(div.xpath('p[1]/text()'))
# print(div.xpath('p[2]/text()'))



import requests
from lxml import etree
def get_html(url):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
    response=requests.get(url,headers=header)
    return response.content.decode('utf-8')

def parse_html(html):
    # 通过xpath提取
    html=etree.HTML(html)
    index=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/i/text()')
    title=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a/text()')
    actor=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[1]/p[2]/text()')
    releasetime=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[1]/p[3]/text()')
    score1=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[2]/p/i[1]/text()')
    score2=html.xpath('/html/body/div[4]/div/div/div[1]/dl/dd/div/div/div[2]/p/i[2]/text()')
    # print(index,title,actor,releasetime,score1,score2)
    tlist=[]
    for i in range(len(index)):
        tlist.append([index[i],title[i],
                      actor[i].strip().replace(",","、").strip("主演："),releasetime[i].strip("上映时间：")
                         ,score1[i]+score2[i]])
    # for line in tlist:
        # print(line)
    return tlist
def save_to_csv(tlist):
    with open("猫眼电影Top100.csv",'a',encoding='utf-8')as f:
       for line in tlist:
           for word in line:
               f.write(word+',')
           f.write('\n')

def main():
    # 清空文本
    with open("猫眼电影Top100.csv",'w',encoding='utf-8')as f:
        f.write('排名,电影名称,主演,上映时间,评分,\n')
    for i in range(10):
        start_url='https://maoyan.com/board/4?offset=%s'%(i*10)
        html=get_html(start_url)
        info=parse_html(html)
        save_to_csv(info)
        print("正在写入第%s页信息..."%(i+1))
main()




























