from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from stores.models import Store


def home(request):
    """views the home page"""
    stores = Store.objects.all()
    return render(request, "home.html", {
        "stores": stores,
    })


def working(request):
    """under construction dialogue"""
    return render(request, 'working.html')


def contact_us(request):
    """This functions lets the user send message to us without logging in."""
    if request.method == "GET":
        ur_name = request.GET.get('ur_name')
        email = request.GET.get('email')
        comment = request.GET.get('comment')

    if email is not None:
        send_mail(ur_name, 'Sent by:' + ur_name + '\nFeedback:' + comment + '\ncontact: ' + email, email,
                  ['dee4code''@gmail.com'])
        return render(request, 'thanks.html')

    return render(request, 'contact_us.html')


@login_required()
def make_money(request):
    return render(request, 'make_money.html')


