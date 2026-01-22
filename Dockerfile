FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY input/ input/
COPY output/ output/

ENV INPUT_FILE=input/kelenfoldig.geojson
ENV OUTPUT_FILE=results/sin_hossz.geojson

CMD ["python", "src/main.py"]