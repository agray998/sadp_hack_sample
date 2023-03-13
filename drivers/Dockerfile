FROM python:3.9

WORKDIR /app

COPY . .
COPY ../models.py ./application

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]