FROM kennethreitz/pipenv

MAINTAINER Bruno Catao

EXPOSE 5002/tcp

COPY src /app

CMD sleep 20; python3 -m saiku.main
