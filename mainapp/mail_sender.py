from django.core.mail import send_mail



send_mail(
    'Test wysyłki email za pośredncitwem django framework',
    'To działa',
    'pythonpetnote@gmail.com',
    ['dobrytyp@gmail.com'],
    fail_silently=False,
)

def send_email(send_mail):
    pass