FROM python:alpine3.19
RUN pip install mysql-connector-python requests flask
ADD . .
EXPOSE 6002
CMD ["python", "-m", "flask", "--app", "timekeeper", "run", "--host=0.0.0.0", "--port", "6002"]