FROM --platform=linux/amd64 python:3.12.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /app/output
CMD ["python", "generate_outputs.py"]
