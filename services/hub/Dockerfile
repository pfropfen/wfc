FROM python:alpine3.19
RUN pip install mysql-connector-python flask pika
ADD . .
EXPOSE 5002
CMD ["python", "-m", "flask", "--app", "hub", "run", "--host=0.0.0.0", "--port", "5002"]
