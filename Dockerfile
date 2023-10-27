FROM python:3.10

WORKDIR /usr/src/app

COPY requirements/prod.txt ./
RUN pip install --no-cache-dir -r prod.txt

COPY . .

CMD [ "python", "app.py" ]