FROM python:3.7

EXPOSE 5000

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

CMD start_dev_server.sh
