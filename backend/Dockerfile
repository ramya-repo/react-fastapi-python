FROM python:3.12.5-slim

WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /api
CMD ["uviorn", "main:app", "--host", "0.0.0.0","--port", "8000"]