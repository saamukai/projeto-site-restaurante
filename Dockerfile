FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        python3-dev libpq-dev postgresql-client  && \
    apt-get clean all  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./django /app

COPY ["./docker/build.sh", "./docker/requirements/requirements.txt", "/tmp/cardapio/"]
RUN sh "/tmp/cardapio/build.sh" && rm -rf "/tmp/cardapio/"

EXPOSE 3000
COPY ./docker/entrypoint.sh /usr/local/bin/
ENTRYPOINT ["sh", "/usr/local/bin/entrypoint.sh"]
