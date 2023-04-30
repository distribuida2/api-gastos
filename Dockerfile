FROM python:3.9

EXPOSE 8000

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000
