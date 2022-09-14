FROM python:3.9.13
ENV PYTHONUNBUFFERED 1
RUN /Growing_Enterprises

WORKDIR /Growing_Enterprises

COPY requirements.txt /Growing_Enterprises/

RUN python -m pip install -r requirements.txt

COPY . /Growing_Enterprises/