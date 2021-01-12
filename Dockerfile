FROM python:3.7.9
LABEL maintainer_name="Omar Magdy"
COPY requirements.txt requirements.txt
ENV SECRET="abcdefg"
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0
CMD ["flask", "run"]