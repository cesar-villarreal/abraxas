FROM python:3.7

ADD . /abraxas

WORKDIR /abraxas

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--chdir", "abraxas/", "abraxas.wsgi"]
