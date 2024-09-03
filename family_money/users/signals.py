from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.signals import user_signed_up
from django.shortcuts import redirect


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.user_profile.save()



@receiver(user_signed_up)
def user_signed_up_redirect(request, user, **kwargs):
    return redirect('common:profile')