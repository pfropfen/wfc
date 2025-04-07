FROM python:alpine3.19
ADD . .
RUN pip install requests pika pandas 
CMD ["python", "worker.py"]
