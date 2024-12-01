FROM python:latest
WORKDIR D:\Github-rep\Proiect_Map
COPY main.py .
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    libfreetype6-dev \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install matplotlib numpy
CMD [ "python","main.py" ]