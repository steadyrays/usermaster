import re
import collections

# 第一步:
# 读取文本内容
f=open('51job岗位信息.txt','r',encoding='utf-8',errors='ignore')
text=f.read()# 读取内容,返回字符串
f.close()

# 第二步:
# 提取所有技能
pattern=re.compile('c\+\+|sql server|[a-zA-Z]+',re.I)
skill_list=re.findall(pattern,text)

# 第三步:
# 将所有字母变成小写
tlist=list(map(lambda x:x.lower(),skill_list))

# 第四步:
# 将字符 'r' 转换为 'R语言'
def rt(data):
    if data=='r':
        return 'R语言'
    else:
        return data
tlist=list(map(rt,tlist))
# print(tlist)

# 第五步:
# 筛选出所需技能
with open('技能词典.txt','r',encoding='utf-8')as f:
    jn=f.read().split(',')
def ft(data):
    if data in jn:# 判断是否是语气词
        return True
    else:
        return False
tlist=list(filter(ft,tlist))
# print(tlist)

"""可以用两种方法对技能信息进行排序,并且写入本地文件"""
"""----------------------开始-------------------------"""
# 方法1:
# skill_dict={}
# for skill in skill_list:
#     if skill in skill_dict:
#         skill_dict[skill]=skill_dict[skill]+1
#     else:
#         skill_dict[skill]=1
# print(skill_dict)

# 方法2(collections统计):
# skill_dict=collections.Counter(tlist)

# # 对字典进行降序排列
# items=skill_dict.items()
# print(sorted(items,key=lambda x:x[1],reverse=True))

# with open('技能统计表.csv','w',encoding='utf-8')as f:
#     for key in skill_dict:
#         print(key,skill_dict[key])
#         f.write(key)
#         f.write(',')
#         f.write(str(skill_dict[key])+'\n')
"""-----------------------结束-------------------------"""

# 第六步:
# 可视化展示(词云图)
from wordcloud import WordCloud
content=' '.join(tlist)# 将列表中的技能连接为字符串类型
# print(content,type(content),len(content))

# wordcloud=WordCloud(
#     width=800,height=400,background_color='white'
# ).generate(content)# 'sql excel sql excel python '
# image=wordcloud.to_image()
# # image.show()
# wordcloud.to_file('class06_词云图.png')

# 词云的参数设置
# wordcloud=WordCloud(
#     width=800,height=600,background_color='white',
#     font_path='C:\\Windows\\Fonts\\msyh.ttc',# 如果存在中文字符需要加载解析的词典
#     max_font_size=500,min_font_size=20
# ).generate(content)
# image=wordcloud.to_image()
# image.show()# 生成图片展示
# wordcloud.to_file('class06_词云图.png')# 在本地生成文件展示


#设置词云背景
import numpy as np
import PIL.Image as img

mask=np.array(img.open('D:\\pycharm\\pycharm_dm\\a课程资料一阶段\\爱心.jpg'))
print(mask)
wordcloud=WordCloud(
    mask=mask,
    width=800,height=600,background_color='white',
    font_path='C:\\Windows\\Fonts\\msyh.ttc',# 如果存在中文字符需要加载解析的词典
    max_font_size=500,min_font_size=20
).generate(content)
image=wordcloud.to_image()
image.show()# 生成图片展示
wordcloud.to_file('词云图.png')# 在本地生成文件展示









