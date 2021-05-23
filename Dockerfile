FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY /. .


RUN apt update 
RUN pip install --upgrade pip && pip install -r requirements.txt 

ENTRYPOINT [ "/app/entrypoint.sh" ]