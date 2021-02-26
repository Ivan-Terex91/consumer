FROM python:3.8
WORKDIR /usr/src/app/

COPY . /usr/src/app/
ENV name_queue=123

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888

CMD ["python", "worker.py"]
