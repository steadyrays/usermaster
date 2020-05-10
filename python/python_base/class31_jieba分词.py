import jieba
# word='我今天不处理逾期信用贷款,因为你们中国银行的APP根本打不开'
# word_list=list(jieba.cut(word))
# print(word_list)
# print('|'.join(jieba.cut(word)))
#
# # 手动添加分离词汇
# jieba.add_word("不处理")
# jieba.add_word("中国银行的APP")
# print('|'.join(jieba.cut(word)))

# 添加词典
job_info="""我们目前正在招聘数据分析师、数据挖掘、数据开发工程师、数据运营,
分别要求本科、研究生、大专及以上学历,最好来自于统计学、数学、计算机相关专业,
具有良好的沟通能力和业务经验
"""
"""未加载字典"""
print('|'.join(jieba.cut(job_info)))

"""加载字典"""
jieba.load_userdict("dict.txt")

print('|'.join(jieba.cut(job_info)))