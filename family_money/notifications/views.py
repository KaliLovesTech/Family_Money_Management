from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse
from financials.models import Bill, SavingsGoal
import datetime

@login_required
def send_upcoming_bills_email_view(request):
    user = request.user
    bills = Bill.objects.filter(user=user, due_date__gte=datetime.now())  # Example filter for upcoming bills

    subject = 'Upcoming Bills Reminder'
    html_message = render_to_string('emails/upcoming_bills_email.html', {'user': user, 'bills': bills})
    plain_message = strip_tags(html_message)
    from_email = 'noreply@your-domain.com'
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    return JsonResponse({'status': 'Email sent successfully'})

@login_required
def send_weekly_digest_email_view(request):
    user = request.user
    accounts = user.accounts.all()  # Example: fetching user's accounts
    investments = user.investments.all()
    goals = SavingsGoal.objects.filter(user=user)

    context = {
        'user': user,
        'accounts': accounts,
        'investments': investments,
        'goals': goals,
    }
    subject = 'Your Weekly Financial Summary'
    html_message = render_to_string('emails/weekly_digest_email.html', context)
    plain_message = strip_tags(html_message)
    from_email = 'noreply@your-domain.com'
    to = user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    return JsonResponse({'status': 'Weekly digest email sent successfully'})