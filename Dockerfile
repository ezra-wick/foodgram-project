FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY /. .


RUN pip install --upgrade pip && pip install -r requirements.txt 

RUN chmod a+x /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]