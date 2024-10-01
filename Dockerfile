FROM python:latest
WORKDIR home/app
COPY . home/app
RUN pip install -r home/app/requirements.txt