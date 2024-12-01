FROM python:latest
WORKDIR D:\Github-rep\Proiect_Map
COPY main.py .
RUN pip install --no-cache-dir matplotlib
RUN apt-get update && apt-get install -y python3-tk xvfb
CMD [ "python","main.py" ]