# my_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
import logging

logger = logging.getLogger("my_app")

@receiver(post_save, sender=Book)
def log_book_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Libro creado: {instance.title} - {instance.author}")
