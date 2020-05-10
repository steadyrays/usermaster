import smtplib
from email.header import Header
from email.mime.text import MIMEText# 文本文件
from email.mime.multipart import MIMEMultipart# html文件
from email.mime.image import MIMEImage# image文件
from email.mime.base import MIMEBase# 发送非文本数据
from email import encoders

def send_email(SMTP_host, from_account, from_password, to_account, subject, content):
    # 1.实例化
    smtp=smtplib.SMTP_SSL(SMTP_host,465)

    # 2.连接服务器
    smtp.connect(SMTP_host,465)
    # smtp.ehlo()
    #smtp.starttls()

    # 3.配置发送邮件的用户名和密码
    smtp.login(from_account,from_password)

    # 4.配置发送内容msg
    msg = MIMEMultipart() # 发送者
    msg.attach(MIMEText(content, 'plain', 'utf-8'))# 主体文件内容
    msg['Subject'] = Header(subject, 'utf-8')# 标题
    msg['From'] = from_account
    # msg['To'] = to_account# 发送多人时不好设置此参数
    # msg['From'] = formataddr(["张三", "920664709@163.com"])# 设置自定的用户名
    # msg['To'] = formataddr(["李四", "920664709@163.com"])# 设置自定的用户名

    '''
    添加文本文件
    '''
    # att1 = MIMEText(open(r'E:\代码\Python文件\课件中心\数据可视化\电子商务数据集.csv', 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # att1["Content-Disposition"] = 'attachment; filename="test.csv"'
    # msg.attach(att1)

    '''
    添加html文件
    '''
    # att2 = MIMEText(open(r'E:\代码\Python文件\数据可视化\render.html', 'r' ,encoding='utf-8').read(), 'base64')
    # att2["Content-Type"] = 'application/octet-stream'
    # # 附件名称非中文时的写法
    # # att2["Content-Disposition"] = 'attachment; filename="Personas.html"'
    # # 附件名称为中文时的写法
    # att2.add_header("Content-Disposition", "attachment", filename=("gbk", "", "用户画像.html"))
    # msg.attach(att2)

    '''
    添加图片(不能修改文件名)
    '''
    # att3= MIMEImage(open("爱心.jpg",'rb').read())
    # att3.add_header('Content-ID', 'imageid')
    # msg.attach(att3)

    '''
    压缩文件
    '''
    att4=MIMEBase('application', 'octet-stream')
    # 加上必要的头信息:
    att4.add_header('Content-Disposition', 'attachment', filename=("gbk", "", '压缩包123.zip'))
    att4.add_header('Content-ID', '<0>')
    att4.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    att4.set_payload(open("./压缩文件.zip",'rb').read())
    encoders.encode_base64(att4)
    msg.attach(att4)

    '''
    添加图片
    '''

    att5 = MIMEBase('application', 'octet-stream')
    # 加上必要的头信息:
    att5.add_header('Content-Disposition', 'attachment',filename=("gbk", "", '爱心.png'))
    att5.add_header('Content-ID', '<0>')
    att5.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    att5.set_payload(open("./爱心.jpg", 'rb').read())
    encoders.encode_base64(att5)
    msg.attach(att5)


    # 5.配置发送邮箱,接收邮箱,以及发送内容
    smtp.sendmail(from_account, to_account, msg.as_string())

    # 6.关闭邮件服务
    smtp.quit()
mail_host='smtp.qq.com'# 服务器地址
sender='543126219@qq.com'# 发送用户
password='noglxallwuypbdef'# 口令
receivers=['543126219@qq.com']# 接收用户可以1个或者多个
# 'wy_cs2433@163.com' '543126219@qq.com' ,'740169097@qq.com','863455565@qq.com'
content="""Dear All:
请查收2019年7月的自动化报表!
"""
send_email(mail_host,sender,password,receivers, "【请知晓】关于Python的邮件自动发送", content)
# 主要参数:服务器地址  发送的邮箱  授权码  接收的邮箱  标题  主体内容