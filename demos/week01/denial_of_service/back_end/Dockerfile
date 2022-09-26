FROM python:alpine
RUN mkdir -p /usr/src/accounts_be
WORKDIR /usr/src/accounts_be
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
