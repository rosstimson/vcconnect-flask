FROM python:3

WORKDIR /usr/src/app

COPY . ./

RUN pip install --no-cache-dir pipenv
RUN pipenv install

EXPOSE 8000

CMD [ "pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "--log-file", "-", "vcconnect-flask:app"]
