FROM python:alpine3.19
ADD . .
RUN pip install mysql-connector-python flask pika
EXPOSE 5002
CMD ["python", "-m", "flask", "--app", "distributor", "run", "--host=0.0.0.0", "--port", "5002"]