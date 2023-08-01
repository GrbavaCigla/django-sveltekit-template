FROM python:3.11

EXPOSE 8000

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app
ENTRYPOINT ["gunicorn"]
CMD ["{{ cookiecutter.project_slug }}.wsgi:application", "--bind", "0.0.0.0:8000"]