#Buscando una imagen que contenga Python y FastAPI me encontre con esto

FROM python:3.9 

#Lo agrego para mejorar la seguiridad
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


#docker build -t test-api-gastos .
#docker run -d --name my-container-api-gastos -p 80:80 test-api-gastos