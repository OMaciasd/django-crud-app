from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

@receiver(post_save, sender=UserProfile)
def log_user_update(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    logger.info(f"UserProfile {action} for user {instance.user.id}")

@receiver(pre_delete, sender=UserProfile)
def log_user_delete(sender, instance, **kwargs):
    logger.info(f"UserProfile about to be deleted for user {instance.user.id}")

class SensitiveData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
