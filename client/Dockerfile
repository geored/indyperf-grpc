FROM python:3.6-slim

WORKDIR /opt/broute
ADD . .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python","client.py"]