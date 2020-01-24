FROM python:3.6

WORKDIR /code
COPY . ./

RUN pip install pipenv
RUN pipenv install
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["bash", "run_server.sh"]
