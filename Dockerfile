FROM python:3.11.1
WORKDIR /code
ADD . .
RUN pip3 install -r requirements.txt
CMD python3 flask_api.py