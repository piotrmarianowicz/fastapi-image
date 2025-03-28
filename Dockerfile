FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY main.py ./

EXPOSE 80

CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "80"]
