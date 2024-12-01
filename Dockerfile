FROM python:latest
WORKDIR D:\Github-rep\Proiect_Map
COPY main.py .
RUN pip install --no-cache-dir matplotlib
EXPOSE 8000
CMD [ "python","main.py" ]