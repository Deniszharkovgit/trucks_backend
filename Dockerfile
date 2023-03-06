FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code
WORKDIR /code
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]