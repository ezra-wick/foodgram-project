FROM python:3.9

ENV PYTHONIOENCODING=utf8

WORKDIR /app
COPY /. .


RUN apt update && apt install wkhtmltopdf -y
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN chmod a+x /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]