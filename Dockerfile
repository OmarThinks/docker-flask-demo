#FROM python:3.7.9 
#LABEL maintainer_name="Omar Magdy"
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#COPY ["src", "/src/"]
#EXPOSE 5000
#ENTRYPOINT ["python", "/src/app.py"]


FROM python:3.7.9
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ENTRYPOINT ["python", "app.py"]