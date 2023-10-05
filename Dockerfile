FROM python:3

ARG ARG_NAME

WORKDIR /std/api_c

COPY requerements.txt ./
RUN pip install --no-cache-dir -r requerements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
