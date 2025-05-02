FROM python:alpine3.19
RUN pip install requests flask openpyxl pandas
ADD . .
EXPOSE 5001
CMD ["python", "-m", "flask", "--app", "distributor", "run", "--host=0.0.0.0", "--port", "5001"]