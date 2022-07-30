FROM python:3.10-alpine

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt 

RUN apk add --no-cache git

RUN apk update && apk add bash 

COPY . . 

CMD ["python3.10", "launcher.py"]