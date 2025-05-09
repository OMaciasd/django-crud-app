FROM python:3.10-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "my_project/manage.py", "runserver", "0.0.0.0:8000"]
