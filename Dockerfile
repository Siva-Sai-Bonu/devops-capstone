FROM python:3.11-slim

WORKDIR /app

RUN pip install prometheus-client --no-cache-dir

COPY app/app.py .

EXPOSE 8080

CMD ["python3", "app.py"]
