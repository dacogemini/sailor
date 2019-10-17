import os

from django.http import HttpResponse

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (From, To, PlainTextContent, HtmlContent, Mail)


def index(request):
    sendgrid_client = SendGridAPIClient(
        api_key=os.environ.get('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'))
    from_email = From('dcollins31@gmail.com')
    to_email = To('dcollins@linuxmail.org')
    subject = 'Sending with Twilio SendGrid is Fun'
    plain_text_content = PlainTextContent(
        'and easy to do anywhere, even with Python'
    )
    html_content = HtmlContent(
        '<strong>and easy to do anywhere, even with Python</strong>'
    )
    message = Mail(from_email, to_email, subject, plain_text_content, html_content)
    response = sendgrid_client.send(message=message)

    return HttpResponse('Email Sent!')
