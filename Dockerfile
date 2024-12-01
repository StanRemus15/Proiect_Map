FROM python:latest
WORKDIR D:\Github-rep\Proiect_Map
COPY main.py .
RUN pip install flask matplotlib numpy

CMD [ "python","main.py" ]