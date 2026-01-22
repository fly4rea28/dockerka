import json
import sys
from shapely.geometry import shape, LineString, MultiLineString

def geometry_length(geom):
    if isinstance(geom, (LineString,MultiLineString)):
        return geom.length
    else:
        return 0.0
    
def main(geojson_path):
    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_length = 0.0
    
    if data["type"] =="FeatureCollection":
        for feature in data["features"]:
            geom = shape(feature["geometry"])
            length = geometry_length(geom)
           total_length += length

    elif data["type"] == "Feature":
        geom = shape(data["geometry"])
        total_length = geometry_length(geom)

    else:
        geom= shape(data)
        total_length =geometry_length(geom)

     print(f"Útszakasz teljes hossza: {total_length: .2f} méter")

    if __name__ == "__main__":
        if len(sys.argv) !=2
            print("Használat: python main.py kelenfoldig.geojson") 
            sys.exit(1)

        main(sys.argv[1])     