from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse


def send_verify_email(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
    from_email = settings.EMAIL_HOST_USER
    subject = f'Активация пользователя {user.username}'.encode('utf-8')
    message = f'Для активации пользователя {user.username} на портале {settings.DOMAIN_NAME} перейдите по ссылке \n' \
              f'{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(subject=subject,
                     message=message,
                     from_email=from_email,
                     recipient_list=[user.email],
                     fail_silently=False)
