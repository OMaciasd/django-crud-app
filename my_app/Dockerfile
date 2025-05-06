FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=my_project.settings \
    PORT=8080

RUN python manage.py collectstatic --noinput \
    && python manage.py migrate

CMD ["gunicorn", "my_project.wsgi:application", "--bind", "0.0.0.0:8000"]

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
