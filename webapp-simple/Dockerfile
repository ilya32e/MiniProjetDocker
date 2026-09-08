# Image de l'exercice 4 : un serveur web Flask dans un conteneur.
FROM python:3.12-slim

LABEL description="Serveur web Flask minimal (exos 3 a 5)"

WORKDIR /srv

# pip install AVANT le COPY du code : la couche est mise en cache et n'est pas
# reconstruite a chaque modification de app.py.
RUN pip install --no-cache-dir flask==3.0.3

COPY app.py .

ENV PORT=5050
EXPOSE 5050

CMD ["python", "app.py"]
