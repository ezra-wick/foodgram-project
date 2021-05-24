FROM python:3.9

ENV PYTHONIOENCODING=utf8

WORKDIR /app
COPY /. .


RUN apt update
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN chmod a+x /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]
# Никак не запускается по ip-адресу...
# Я надеялся вы мне поможете
# slack уже не работает...