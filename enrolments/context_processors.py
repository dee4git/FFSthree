from .models import ExtendedUser, Enrolment


def extras(request):
    extended_user = 0
    try:
        enrolled_user = ExtendedUser.objects.get(user=request.user)
        if enrolled_user is not None:
            extended_user = 1
    except:
        extended_user = 0
    return {"extended_user": extended_user}


def enrolment(request):
    has_enrolment = 0
    try:
        enrolled_user = ExtendedUser.objects.get(user=request.user)
        enrolments = Enrolment.objects.filter(user=enrolled_user)
        if enrolments is not None:
            has_enrolment = 1
    except:
        has_enrolment = 0
    return {"has_enrolment": has_enrolment}