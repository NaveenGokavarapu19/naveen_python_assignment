FROM python:3.8.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ../src src
EXPOSE 5001
ENTRYPOINT ["python","./src/app.py"]