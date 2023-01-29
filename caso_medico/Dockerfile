# Singer Back-end for prod
# Version: 1.0
FROM python:3.10-slim-buster
# copy source code
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# add entry point script
COPY . .

EXPOSE 80

CMD [ "python3", "-m" , "uvicorn", "app.main:app", "--proxy-headers", "--host=0.0.0.0", "--port=80"]