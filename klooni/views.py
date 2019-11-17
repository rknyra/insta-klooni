from django.shortcuts import render
from django.contrib.auth import login, views, forms


#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', {'form':form})