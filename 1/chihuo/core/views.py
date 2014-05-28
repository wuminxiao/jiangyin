from django.http import HttpResponse




def access_verify(r):
    return HttpResponse('token')
