FROM python:3.7.9 

LABEL maintainer_name="Omar Magdy"


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]