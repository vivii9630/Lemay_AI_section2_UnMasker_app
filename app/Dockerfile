FROM python:3.6
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
#COPY dist/ ./dist/
#COPY requirements.txt/app/requirements.txt
EXPOSE 5000

CMD [ "python", "wsgi.py"]