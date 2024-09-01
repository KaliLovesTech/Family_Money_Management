from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from datetime import datetime



# Profile View
@login_required
def profile_view(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('common:profile')
        else:
            print(profile_form.errors)  # Print errors to diagnose issues

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'common/profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important to keep the user logged in after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('common:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'common/change_password.html', {'form': form})



# Dashboard View
@login_required
def dashboard_view(request):
    # Example data to be passed to the template
    account_balance = 12345.67
    savings_goals = 3456.78
    upcoming_bills = 789.01
    
    # Example transactions data
    recent_transactions = [
        {'date': '2024-08-30', 'description': 'Grocery Store', 'category': 'Groceries', 'amount': -123.45},
        {'date': '2024-08-29', 'description': 'Salary', 'category': 'Income', 'amount': 2000.00},
        {'date': '2024-08-28', 'description': 'Electric Bill', 'category': 'Utilities', 'amount': -150.00},
    ]

    # Example savings goals progress data
    savings_goals_progress = [
        {'name': 'Vacation Fund', 'progress': 70},
        {'name': 'Emergency Fund', 'progress': 45},
        {'name': 'New Car Fund', 'progress': 25},
    ]

    # Example upcoming bills data
    upcoming_bills_list = [
        {'name': 'Rent', 'amount': 1200.00, 'due_date': datetime(2024, 9, 5)},
        {'name': 'Internet', 'amount': 50.00, 'due_date': datetime(2024, 9, 10)},
        {'name': 'Credit Card', 'amount': 200.00, 'due_date': datetime(2024, 9, 15)},
    ]

    # Example budget overview data
    monthly_budget = 3000.00
    spent_this_month = 2500.00
    budget_progress = (spent_this_month / monthly_budget) * 100

    context = {
        'account_balance': account_balance,
        'savings_goals': savings_goals,
        'upcoming_bills': upcoming_bills,
        'recent_transactions': recent_transactions,
        'savings_goals_progress': savings_goals_progress,
        'upcoming_bills_list': upcoming_bills_list,
        'monthly_budget': monthly_budget,
        'spent_this_month': spent_this_month,
        'budget_progress': budget_progress,
    }

    return render(request, 'common/dashboard.html', context)