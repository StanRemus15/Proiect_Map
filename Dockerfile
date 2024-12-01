FROM python:latest
WORKDIR D:\Github-rep\Proiect_Map
COPY main.py .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python","main.py" ]