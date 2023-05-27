FROM postgres:latest

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

ADD settings/init.sql /docker-entrypoint-initdb.d
