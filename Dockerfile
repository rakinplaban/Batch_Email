FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /Batch_Email
COPY requirements.txt /Batch_Email/
RUN pip install -r requirements.txt
COPY . /Batch_Email/