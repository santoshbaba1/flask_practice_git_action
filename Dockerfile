FROM python:3

WORKDIR /flask

RUN mkdir -p flask

COPY . /flask


RUN  pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r /flask/requirements.txt


EXPOSE 5000

CMD ["python3","/flask/app.py"]

