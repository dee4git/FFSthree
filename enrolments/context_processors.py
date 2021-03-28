from .models import ExtendedUser


def extras(request):
    extended_user = 0
    try:
        extends = ExtendedUser.objects.get(user=request.user)
        if extends is not None:
            extended_user = 1
    except:
        extended_user = 0
    return {"extended_user": extended_user}

