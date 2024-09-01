from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.shortcuts import redirect

@receiver(user_signed_up)
def user_signed_up_redirect(request, user, **kwargs):
    return redirect('common:profile')