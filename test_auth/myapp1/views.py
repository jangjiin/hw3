from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
   return HttpResponse('<p>click <a href="/admin/login/">here</a> to login.</p><p><h1>auth required</h1>')

