FROM python:alpine3.19
ADD . .
RUN pip install pandas flask openpyxl
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "distributor", "run", "--host=0.0.0.0", "--port", "5000"]