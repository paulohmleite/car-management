# syntax=docker/dockerfile:1
FROM python:3.10.1-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pytest --cov .
EXPOSE 5000
COPY . .
# CMD ["flask", "run"]
CMD ["py", "main.py"]