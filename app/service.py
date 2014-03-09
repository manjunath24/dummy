from django.conf import settings

from django.core.mail import EmailMessage 


class UserService:
    def __init__(self, email, code):
        self.email = email
        self.code = code

    def send_activation_link(self):
        subject = 'Activation Link'
        body = 'Dear %s click on the link to activate your account \
                http://127.0.0.1:8080/confirm/?user=%s' % (self.email, self.code)
        msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [self.email])
        msg.send()

