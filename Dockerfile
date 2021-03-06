FROM python:3.8-slim-buster

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000
ENTRYPOINT [ "python", "app.py"]

