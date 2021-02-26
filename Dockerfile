FROM python:3.9

WORKDIR /usr/src/app

ENTRYPOINT ["python"]

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["minips/main.py"]

