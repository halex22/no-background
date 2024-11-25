FROM python:3.11-slim

COPY u2net.onnx /home/.u2net/u2net.onnx

WORKDIR /app

ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .



RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "--reload", "app:app" ]