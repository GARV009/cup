FROM python:3.11


RUN apt-get update && apt-get install -y libpq-dev build-essential


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY="abcd1234"
ENV SQLALCHEMY_TRACK_MODIFICATIONS="False"


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 6500

CMD ["python", "src/app.py"]