from django.contrib import admin
from .models import Book, UserProfile
import logging

crud_logger = logging.getLogger('crud_logger')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Muestra solo el nombre del usuario

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        user = request.user.username if request.user.is_authenticated else 'anónimo'
        crud_logger.info(f"Libro creado por {user}: {obj.titulo} - {obj.autor}")

admin.site.register(Book, BookAdmin)
