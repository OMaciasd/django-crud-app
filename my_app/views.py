from .models import UserProfile
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
import logging
from django.contrib.auth.decorators import login_required
from datetime import datetime

logger = logging.getLogger('crud_logger')

class BookAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        user = request.user.username if request.user.is_authenticated else 'anónimo'
        crud_logger.info(f"Libro creado por {user}: {obj.titulo} - {obj.autor}")

def crear_libro(request):
    if request.method == 'POST':
        # ... lógica de creación ...
        libro = Libro.objects.create(titulo="Loki", autor="jrr Tolkien")
        usuario = request.user.username if request.user.is_authenticated else 'anónimo'
        crud_logger.info(f"Libro creado por {usuario}: {libro.titulo} - {libro.autor}")

def some_view(request):
    logger.debug('Se ha creado un nuevo libro')  # Esto aparecerá en los logs
    return HttpResponse("Operación completada.")

def test_logging(request):
    logger.info('Este es un mensaje de log desde la vista test_logging')
    return HttpResponse('Logging test successful')

@login_required
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            logger.info(f"[{datetime.now().isoformat()}] Libro creado por {request.user.username}: {book.title} - {book.author}")
            return redirect('book_list')

def my_view(request):
    logger.info("Se ha accedido a la vista my_view")  # Mensaje de log de nivel INFO
    return HttpResponse("Vista con logging.")

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            logger.info(f"[{request.user}] creó el libro: {book.title} ({book.pk})")
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'my_app/book_form.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # Lógica de edición
    logger.info(f"Se editó el libro con título: {book.title} por {book.author}")
    return redirect('book_list')

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # Lógica para eliminar un libro
    logger.warning(f"Se eliminó el libro con título: {book.title}")
    return redirect('book_list')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'my_app/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            logger.info(f"[{request.user}] creó el libro: {book.title} ({book.pk})")  # ← aquí
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'my_app/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'my_app/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'my_app/book_confirm_delete.html', {'book': book})

def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

def activity_dashboard(request):
    # Aquí puedes obtener las últimas entradas de logs o datos de performance
    activities = Book.objects.all()  # O cualquier otro dato relevante

    # Puedes incluir la información de los logs si estás usando Django Logging
    logger.info("Mostrando el dashboard de actividades")

    return render(request, 'activity_dashboard.html', {'activities': activities})
