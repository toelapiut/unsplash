from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context


def send_welcome_email(name,reciever):
    #creating message subject and sender

    subject='Welcome to unsplash Newsletter'
    sender='toelapiut7@gmail.com'



    #passing in the context variables
    text_context=render_to_string('email/infoemail.txt',{"name":name})
    html_context=render_to_string('email/infoemail.html',{'name':name})


    msg=EmailMultiAlternatives(subject,text_context,sender,[reciever])
    msg.attach_alternative(html_context,'text/html')
    msg.send()