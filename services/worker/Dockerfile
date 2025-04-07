FROM python:alpine3.19
ADD . .
RUN pip install requests pika 
CMD ["python", "worker.py"]