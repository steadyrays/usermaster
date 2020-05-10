import jieba# 分词模块
import re
import collections
f=open('51job岗位信息.txt','r',encoding='utf-8',errors='ignore')
text=f.read()# 读取文件
f.close()
pattern='[^0-9a-zA-Z\W_]+'
job_info=re.findall(pattern,text)# 返回列表

result=list(jieba.cut(' '.join(job_info)))# 将字符串中的常见词频提取,并返回字符串
# print(list(result))
print(collections.Counter(result))

# 设置词云背景
import numpy as np# pip install numpy
import PIL.Image as img# pip install PIL
from wordcloud import WordCloud
mask=np.array(img.open('D:\\pycharm\\pycharm_dm\\a课程资料一阶段\\爱心.jpg'))
# print(mask)
wordcloud=WordCloud(
    mask=mask,
    width=800,height=600,background_color='white',
    font_path='C:\\Windows\\Fonts\\msyh.ttc',# 如果存在中文字符需要加载解析的词典
    max_font_size=500,min_font_size=20
).generate(' '.join(result))
image=wordcloud.to_image()
# image.show()# 生成图片展示
wordcloud.to_file('岗位要求词云图.png')# 在本地生成文件展示













