from django.shortcuts import render
from travelpack.models import Destination

# Create your views here.
def register(request):
    dests = Destination.objects.all()
    
    return render(request, 'accounts/register.html', {'dests': dests})
    