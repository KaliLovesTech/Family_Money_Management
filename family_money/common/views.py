from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import views

@login_required
def dashboard_view(request):
    # The data fetching will be handled by the front-end calling the respective APIs
    return render(request, 'common/dashboard.html')