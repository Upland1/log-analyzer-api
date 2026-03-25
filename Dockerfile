FROM python:3.10-slim

WORKDIR /app

# copy dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

#run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
