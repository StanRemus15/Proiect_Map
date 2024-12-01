FROM python:latest
WORKDIR D:\Github-rep\Proiect_Map
COPY main.py .
RUN pip install --no-cache-dir matplotlib
RUN apt-get update && apt-get install -y \
    python3-tk \
    libxrender1 \
    libx11-6 \
    libxext6 \
    x11-utils \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

CMD [ "python","main.py" ]