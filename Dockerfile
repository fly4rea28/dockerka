FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir shapely

COPY src/ src/
COPY input/ input/
COPY output/ output/

ENTRYPOINT [ "pyton", "src/main.py" ]