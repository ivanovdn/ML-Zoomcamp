FROM python:3.8.12-slim

WORKDIR /app

COPY predict.py /app
COPY capstone_model.pkl /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]