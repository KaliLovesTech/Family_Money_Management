from django.shortcuts import render, get_object_or_404, redirect

def dashboard_view(request):
    # The data fetching will be handled by the front-end calling the respective APIs
    return render(request, 'common/dashboard.html')

    