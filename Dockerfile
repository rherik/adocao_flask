FROM python:3.10-slim

EXPOSE 5000

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

COPY . .

CMD ["/bin/bash", "docker_entrypoint.sh"]
