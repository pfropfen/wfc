FROM python:alpine3.19
RUN pip install requests pika pandas
ADD . .
CMD ["python", "worker.py"]
