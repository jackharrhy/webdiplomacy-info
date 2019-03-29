FROM python:3-alpine

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY . /app
COPY .env.dist /app/.env

WORKDIR /app
CMD ["python", "remind.py"]
