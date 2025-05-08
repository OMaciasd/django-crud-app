from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import logging
from django.contrib.auth.models import User

logger = logging.getLogger("my_app")

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}"

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

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()  # Este campo debe estar presente
    isbn = models.CharField(max_length=13)  # Este campo debe estar presente

    def __str__(self):
        return self.title
