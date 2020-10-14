FROM python:3.8.1-slim-buster
EXPOSE 8000
ENV PYTHONUNBUFFERED=1 \
    PORT=8000
WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
