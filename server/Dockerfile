FROM python:3.6-slim

WORKDIR /opt/broute
ADD . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8081 50051
CMD ["python","server.py"]