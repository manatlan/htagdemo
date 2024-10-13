FROM python:3.12-slim
EXPOSE 8000
WORKDIR /usr/src/app
# COPY app_simple/ .
COPY app_demo/ .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "server.py"]