FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY smartnomad-core/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY smartnomad-core/ /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]