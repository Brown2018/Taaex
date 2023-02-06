import os
from django.conf import settings
import smtplib
from email.message import EmailMessage

class dao_sendMailConfirmationCount(object):
    @staticmethod
    def sendMailCoordonnes(username,password,entreprise,to='kandealex007@gmail.com'):
        try:
            EMAIL_ADRESS=settings.EMAIL_HOST_USER
            
            EMAIL_PASSWORD=settings.EMAIL_HOST_PASSWORD
            EMAIL_HOST=settings.EMAIL_HOST
            EMAIL_POSRT=settings.EMAIL_PORT
            HOST=settings.HOST
            msg=EmailMessage()

            msg['Subject']='CONFIRMATION CLIENT\'S ACCOUNT'
            msg['From']=EMAIL_ADRESS
            msg['To']=to

            msg.set_content('This helps you to confirme your account by clicking in this link bellow !')
            msg.add_alternative("""\

          <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
                <title>Mail</title>
            </head>
            
            <body>
                
                <header style="border 1 solide">
                    <img class="fluid" src="https://tkngomedia.s3.eu-west-3.amazonaws.com/static/Mail.png" alt="">
                </header>
            
             <main>
        <h1 class="title is-size-2 has-text-centered">"""+entreprise+"""</h1>   

             
            <div class="row">
        
        <center>
                <p > 
                        User :'"""+username+"""'
                        Password :'"""+password+"""'
                </p>
        </center>
        </div>
    </main>

            </body>
            </html>


                """,subtype='html')
      

            with smtplib.SMTP_SSL(str(EMAIL_HOST),EMAIL_POSRT) as smtp:
                smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
                smtp.ehlo()
                smtp.send_message(msg)

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def sendMaimConfCount(id,to='kandealex007@gmail.com'):
        try:
            EMAIL_ADRESS=settings.EMAIL_HOST_USER
            
            EMAIL_PASSWORD=settings.EMAIL_HOST_PASSWORD
            EMAIL_HOST=settings.EMAIL_HOST
            EMAIL_POSRT=settings.EMAIL_PORT
            HOST=settings.HOST
            msg=EmailMessage()

            msg['Subject']='CONFIRMATION CLIENT\'S ACCOUNT'
            msg['From']=EMAIL_ADRESS
            msg['To']=to

            msg.set_content('This helps you to confirme your account by clicking in this link bellow !')
            msg.add_alternative("""\

          <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
                <title>Mail</title>
            </head>
            
            <body>
                
                <header style="border 1 solide">
                    <img class="fluid" src="https://tkngomedia.s3.eu-west-3.amazonaws.com/static/Mail.png" alt="">
                </header>
            
             <main>
        <h1 class="title is-size-2 has-text-centered"></h1>   

            <p class="is-capitalized has-text-centered"></p>
            <div class="row">
        
        <center>
        <a href='"""+HOST+"""security/activationUser/?user="""+str(id)+"""' >
            <img style="height:100px;width:300px" class="fluid"src="https://tkngomedia.s3.eu-west-3.amazonaws.com/static/button.png" alt="">
        </a>
        </center>
        </div>
    </main>

            </body>
            </html>


                """,subtype='html')
      

            with smtplib.SMTP_SSL(str(EMAIL_HOST),EMAIL_POSRT) as smtp:
                smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
                smtp.ehlo()
                smtp.send_message(msg)

            return 1
        except Exception as e:
            return 0

    @staticmethod
    def sendingMail(message,to):
        try:
            EMAIL_ADRESS=settings.EMAIL_HOST_USER
            
            EMAIL_PASSWORD=settings.EMAIL_HOST_PASSWORD
            EMAIL_HOST=settings.EMAIL_HOST
            EMAIL_POSRT=settings.EMAIL_PORT
            HOST=settings.HOST
            msg=EmailMessage()

            msg['Subject']='INITIALIZATION OF  CLIENT\'S ACCOUNT PASSWORD'
            msg['From']=EMAIL_ADRESS
            msg['To']=to

            msg.set_content('',message)
            msg.add_alternative("""\

             <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Tklogiciel</title>
            <!-- CSS only -->
            <link rel="stylesheet" href="https://mesmediastatic.s3-us-west-1.amazonaws.com/bootstrap-4.5.2-dist/css/bootstrap.min.css" media="all">

            </head>
            <body>
                <div class="container-fluid">
                    <header style="margin-bottom: 1.8em;"> 
                        <nav class="navbar navbar-d navbar-dark" style="background-color: rgb(43, 63, 85);" >
                            <a class="navbar-brand"  href=\""""+HOST+"""\">
                            <img src="https://mesmediastatic.s3-us-west-1.amazonaws.com/TKLLOGO.png" width="50" height="50" class="d-inline-block align-top" alt="" loading="lazy">
                            TKlogiciel
                            </a>
                        </nav>
                    </header>
            
                    <body>
                        <!-- jumbotron -->
                        <div class="jumbotron" style=" color: white;background-color: rgb(43, 63, 85);">
                            <h1 class="display-4"><strong>Hello, Dear User of Tklogiciel!</strong></h1>
                                <p class="lead"><strong>This is a simple Notification unit, to notice an update of your members</strong></p>
                                <hr class="my-4" style="background: white;">
                                <p><strong>To see More, Sign in to your account</strong></p>
                            <a class="btn btn-primary btn-lg"  href=\""""+HOST+"""\" role="button"><strong>Sign In</strong></a>
                        </div>
                         <h1 style="color:SlateGray;">"""+message+""" </h1>
                        <!-- / jumbotron -->
                       
                    </body>
                
                         <br><br>
                    <footer>
                        <div style="background-color: rgb(43, 63, 85);">
                            <center><a style="color: white;"  href=\""""+HOST+"""\"><strong>www.tklogiciel.com</strong></a></center>
                        </div>
                    </footer>
                </div>
                <!-- JS, Popper.js, and jQuery -->

            </body>
            </html>
                       
            """,subtype='html')
      
            with smtplib.SMTP_SSL(str(EMAIL_HOST),EMAIL_POSRT) as smtp:
                smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
                smtp.ehlo()
                smtp.send_message(msg)

            return str("Message sent successfully")
        except Exception as e:
            return str("something went wrong "+e)

    @staticmethod
    def sendingMailMultipleRecipient(username,action,message,recipient):
        try:
            EMAIL_ADRESS=settings.EMAIL_HOST_USER
            #HOST=settings.HOST_MEDIA
            #print(HOST+""+message)
            HOST=settings.HOST
            
            EMAIL_PASSWORD=settings.EMAIL_HOST_PASSWORD
            EMAIL_HOST=settings.EMAIL_HOST
            EMAIL_POSRT=settings.EMAIL_PORT
            msg=EmailMessage()

            msg['Subject']='NOTIFICATION'
            msg['From']=EMAIL_ADRESS
            msg['To']=", ".join(recipient)

            msg.set_content('',message)
            msg.add_alternative("""\
          <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Tklogiciel</title>
            <!-- CSS only -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">

            </head>
            <body>
                <div class="container-fluid">
                    <header style="margin-bottom: 1.8em;"> 
                        <nav class="navbar navbar-d navbar-dark" style="background-color: rgb(43, 63, 85);" >
                            <a class="navbar-brand" href=\""""+HOST+"""\">
                            <img src="https://mesmediastatic.s3-us-west-1.amazonaws.com/TKLLOGO.png" width="50" height="50" class="d-inline-block align-top" alt="" loading="lazy">
                            TKlogiciel
                            </a>
                        </nav>
                    </header>
            
                    <body>
                        <!-- jumbotron -->
                        <div class="jumbotron" style=" color: white;background-color: rgb(43, 63, 85);">
                            <h1 class="display-4"><strong>Hello, Dear User of Tklogiciel!</strong></h1>
                                <p class="lead"><strong>This is a simple Notification unit, to notice an update of your members</strong></p>
                                <hr class="my-4" style="background: white;">
                                <p><strong>To see More, Sign in to your account</strong></p>
                            <a class="btn btn-primary btn-lg"  href=\""""+HOST+"""\" role="button"><strong>Sign In</strong></a>
                        </div>
                         <h1 style="color:SlateGray;">"""+action+""" </h1>
                        <!-- / jumbotron -->
                        <div class="card" style="width: 18rem;">
                            <img class="card-img-top" src=\""""+message+"""\"/>
                            <div class="card-body">
                            <h5 class="card-title" style="color:SlateGray;">A Post</h5>
                            <p class="card-text"></p>
                            <a href=\""""+HOST+"""\" class="btn btn-primary"><strong>Go To Tklogiciel</strong></a>
                            </div>
                        </div>
                    </body>
                      <br><br>
                        
                    <footer >
                        <div style="background-color: rgb(43, 63, 85);">
                            <center><a style="color: white;"  href=\""""+HOST+"""\"><strong>www.tklogiciel.com</strong></a></center>
                        </div>
                    </footer>
                </div>
                <!-- JS, Popper.js, and jQuery -->

            </body>
            </html>
                       
                """,subtype='html')

            with smtplib.SMTP_SSL(str(EMAIL_HOST),EMAIL_POSRT) as smtp:
                smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
                smtp.ehlo()
                smtp.send_message(msg)

            return str("Message sent successfully")
        except Exception as e:
            return str("something went wrong "+e)



    @staticmethod
    def sendingMailMultipleRecipient_noImage(username,action,message,recipient):
        try:
            EMAIL_ADRESS=settings.EMAIL_HOST_USER
            #HOST=settings.HOST_MEDIA
            #print(HOST+""+message)
            HOST=settings.HOST
            
            EMAIL_PASSWORD=settings.EMAIL_HOST_PASSWORD
            EMAIL_HOST=settings.EMAIL_HOST
            EMAIL_POSRT=settings.EMAIL_PORT
            msg=EmailMessage()

            msg['Subject']='NOTIFICATION'
            msg['From']=EMAIL_ADRESS
            msg['To']=", ".join(recipient)
            #msg['To']="kandealex007@gmail.com"

            msg.set_content('',message)
            msg.add_alternative("""\
          <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Tklogiciel</title>
            <!-- CSS only -->
            <link rel="stylesheet" href="https://mesmediastatic.s3-us-west-1.amazonaws.com/bootstrap-4.5.2-dist/css/bootstrap.min.css" media="all">

            </head>
            <body>
                <div class="container-fluid">
                    <header style="margin-bottom: 1.8em;"> 
                        <nav class="navbar navbar-d navbar-dark" style="background-color: rgb(43, 63, 85);" >
                            <a class="navbar-brand"  href=\""""+HOST+"""\">
                            <img src="https://mesmediastatic.s3-us-west-1.amazonaws.com/TKLLOGO.png" width="50" height="50" class="d-inline-block align-top" alt="" loading="lazy">
                            TKlogiciel
                            </a>
                        </nav>
                    </header>
            
                    <body>
                        <!-- jumbotron -->
                        <div class="jumbotron" style=" color: white;background-color: rgb(43, 63, 85);">
                            <h1 class="display-4"><strong>Hello, Dear User of Tklogiciel!</strong></h1>
                                <p class="lead"><strong>This is a simple Notification unit, to notice an update of your members</strong></p>
                                <hr class="my-4" style="background: white;">
                                <p><strong>To see More, Sign in to your account</strong></p>
                            <a class="btn btn-primary btn-lg"  href=\""""+HOST+"""\" role="button"><strong>Sign In</strong></a>
                        </div>
                         <h1 style="color:SlateGray;">"""+action+""" </h1>
                        <!-- / jumbotron -->
                       
                    </body>
                
                         <br><br>
                    <footer>
                        <div style="background-color: rgb(43, 63, 85);">
                            <center><a style="color: white;"  href=\""""+HOST+"""\"><strong>www.tklogiciel.com</strong></a></center>
                        </div>
                    </footer>
                </div>
                <!-- JS, Popper.js, and jQuery -->

            </body>
            </html>
                       
                """,subtype='html')

            with smtplib.SMTP_SSL(str(EMAIL_HOST),EMAIL_POSRT) as smtp:
                smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
                smtp.ehlo()
                smtp.send_message(msg)

            return str("Message sent successfully")
        except Exception as e:
            return str("something went wrong "+e)