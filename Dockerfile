FROM kennethreitz/pipenv

MAINTAINER Bruno Catao

EXPOSE 5002/tcp

COPY src /app

CMD python3 -m saiku.main