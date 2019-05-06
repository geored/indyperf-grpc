FROM python:3.7

WORKDIR /opt/broute
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
ADD brouteclient/ .
CMD ["python","./client.py"]