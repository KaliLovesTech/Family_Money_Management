from django.shortcuts import render

def dashboard(request):
    # Logic for dashboard view
    return render(request, 'common/dashboard.html')

def profile(request):
    # Logic for user profile view
    return render(request, 'common/profile.html')
