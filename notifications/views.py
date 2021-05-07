from django.shortcuts import render


# Create your views here.
def test_notification(request):
    return render(request, 'toast.html')
