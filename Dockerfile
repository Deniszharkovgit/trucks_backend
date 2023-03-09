FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]