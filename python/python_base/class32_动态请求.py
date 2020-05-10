# 分析请求
"https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0"
"https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=20"
"https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=40"
"https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=60"
import requests
import json
with open('豆瓣选电影.csv', 'w', encoding='utf-8-sig')as f:
    f.write('电影编号,电影评分,电影名称,电影链接,封面链接,\n')

for i in range(15):
    start_url='https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start={}'.format(20*i)
    response=requests.get(start_url)
    content=response.content.decode('utf-8')
    # print(content)
    # print(type(content))

    """解析json文件"""
    data=json.loads(content)

    # print(data)
    # print(type(data))
    info=[]
    for film in data['subjects']:
        info.append([film['id'],film['rate'],film['title'],film['url'],film['cover']])
    print(info)

    with open('豆瓣选电影.csv','a',encoding='utf-8-sig')as f:
        for line in info:
            for word in line:
                f.write(word+',')
            f.write('\n')



"http://p3.pstatp.com/origin/pgc-image/f2edb44479d7454c8f91874d0d6a6524"
"//p3.pstatp.com/list/pgc-image/3d89978eb4e74a12a67b813191f8b76e"