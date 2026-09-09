FROM python:3.12-slim

LABEL description="Serveur web Flask minimal (exos 3 a 5)"

WORKDIR /srv

RUN pip install --no-cache-dir flask==3.0.3

COPY app.py .

ENV PORT=5050
EXPOSE 5050

CMD ["python", "app.py"]
