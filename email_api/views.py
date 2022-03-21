from socket import send_fds
from django.shortcuts import render
import smtplib
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework import status
from rest_framework import permissions


class EmaiApi(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"username" : "ENTER_YOUR_USERNAME","send_to":"ENTER_RECIEVER_EMAIL_ADDRESS"})
    def post(self,request,*args,**kwargs):
        username = request.data.get('username')
        send_to =  request.data.get('send_to')
        print(username,send_to)
        gmail_user = 'naoem777@gmail.com'
        gmail_password = 'ily@kashur_cheena2'
        mail_content =html = """\
        <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>

    <!-- Bootstrap -->
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
     <img src="https://thumbs.dreamstime.com/b/welcome-board-lifebuoy-text-wooden-background-horizontal-copy-space-individual-86816637.jpg" style="width:100%"/>
    <h1 style="text-align:center">Welcome {0} 🎉</h1>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
  </body>
</html>
        """.format(username)
        message = MIMEMultipart()
        message['From'] = gmail_user
        message['To'] = send_to
        message['Subject'] = 'Django Mailing Webserver'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            text = message.as_string()
            smtp_server.sendmail(gmail_user, send_to, text)
            smtp_server.close()
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….",ex)
        return Response("Email Sent Succesfully",status=status.HTTP_201_CREATED)