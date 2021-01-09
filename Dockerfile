FROM python:3.7.9 

LABEL maintainer_name="Omar Magdy"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ["src", "/src/"]

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]