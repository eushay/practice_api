FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /practice_api

COPY . /practice_api/

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /practice_api

CMD [ "uvicorn", "my_app.main:app", "--host", "0.0.0.0", "--port", "8001"]