from gmail import GMail, Message
from random import choice
import datetime
now = datetime.datetime.now()
#giao thuc smtp

html_template = '''
<p><em>Hi Sếp,</em> h&ocirc;m nay em bị {{sickness}} &nbsp;</p>
<p>Mong sếp cho em nghỉ ph&eacute;p ng&agrave;y 24/4/2018.</p>
<p>Em xin cảm ơn.&nbsp;</p>'''
sickness_list = ["thương hàn","kiết lị","sốt cao","đau răng", "sốt virus", "thủy đậu"]
sick = choice(sickness_list)

html_content = html_template.replace("{{sickness}}",sick)
gmail = GMail('oanhharry123@gmail.com','toilatoi@123')
msg = Message('Xin nghi le',to='C4E <c4e.201708@gmail.com>',html=html_content)

loop = True
while loop:
    if now.hour == 7 and now.minute == 0:
        gmail.send(msg)
        loop = False
