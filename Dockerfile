FROM python:3

COPY requirenents.txt .

RUN pip install -r requirements

COPY main.py .

CMD [ "python", "./main.py" ]
