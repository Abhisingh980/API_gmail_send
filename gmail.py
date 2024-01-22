import smtplib
import ssl


def send_mail(message):
    host_name = "smtp.gmail.com"
    port = 465
    user_name = "kr.abhinesh147@gmail.com"
    password = "airi ccif mmkn paol"
    receiver = "deepabhineshacp@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host=host_name, port=port, context=context) as send:
        send.login(user_name, password)
        send.sendmail(user_name, receiver, message)


