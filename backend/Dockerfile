FROM python:3.14.3

WORKDIR /backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 2307

CMD ["python", "manage.py", "runserver", "0.0.0.0:2307", "--noreload"]
