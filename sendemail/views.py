from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        # runs validation routines for all its fields
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['dcollins@linuxmail.org'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


<<<<<<< HEAD
def successView(request):
    template = loader.get_template("../templates/success.html")
    return HttpResponse(template.render())
=======
def index(request):
    sendgrid_client = SendGridAPIClient(
        api_key=os.environ.get('xxxxxxxxxxxxxxxxxxxxx'))
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
>>>>>>> 4a16bd183bd7af626d6c4a3d63d955a70f3cc28d
