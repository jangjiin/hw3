from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
   return HttpResponse('<p>click <a href="/admin/logout/">here</a> to logout.</p><p><h1>auth success!</h1>')

