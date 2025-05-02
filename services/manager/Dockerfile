FROM python:alpine3.19
RUN pip install pandas flask openpyxl
ADD . .
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "manager", "run", "--host=0.0.0.0", "--port", "5000"]
