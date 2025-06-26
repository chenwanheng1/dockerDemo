FROM python:3.6

WORKDIR ./dockerDemo

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]