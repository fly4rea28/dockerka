import os
import geopandas
import pandas

#mappazas
INPUT_FILE = os.getenv("INPUT_FILE", "input/kelenfoldig.geojson")
OUTPUT_GEOJSON = os.getenv("OUTPUT_GEOJSON", "output/sin_hossz.geojson")
OUTPUT_CSV = os.getenv("OUTPUT_CSV", "output/sin_hossza.csv")

print(f"Sín hálózat betöltése: {INPUT_FILE}")
grf = geopandas.read_file(INPUT_FILE)

print(f"Vetület vizsgálat")

#Vizsgálat
if grf.crs.to_string() == "EPSG:23700":
    print("Jó a vetület")
    grf = grf.to_crs(epsg=23700)
#Összes szakasz hossza
grf["length_m"] = grf.geometry.length

#teljes hossz
teljes_hossz = grf["length_m"].sum()
teljes_kmben = teljes_hossz / 1000

#mentés
pandas.DataFrame([{"teljes_sin_hossza": teljes_hossz}]).to_csv(OUTPUT_CSV, index=False)
print(f"Teljes sín hossza méterben mentve: {OUTPUT_CSV}")

#eredmény
print(f"Teljes sín hossz: {teljes_hossz: .2f} méter")
print(f"Teljes hossz km-ben: {teljes_kmben: .2f} km")




#korábbi próbálkozás 
#def geometry_length(geom):
#    if isinstance(geom, (LineString,MultiLineString)):
#        return geom.length
#     else:
#         return 0.0
#     
# def main(geojson_path):
#     with open(geojson_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
# 
#     total_length = 0.0
#     
#     if data["type"] =="FeatureCollection":
#         for feature in data["features"]:
#             geom = shape(feature["geometry"])
#             length = geometry_length(geom)
#            total_length += length
# 
#     elif data["type"] == "Feature":
#         geom = shape(data["geometry"])
#         total_length = geometry_length(geom)
# 
#     else:
#         geom= shape(data)
#         total_length =geometry_length(geom)
# 
#      print(f"Útszakasz teljes hossza: {total_length: .2f} méter")
# 
#     if __name__ == "__main__":
#         if len(sys.argv) !=2
#             print("Használat: python main.py kelenfoldig.geojson") 
#           sys.exit(1)
#
#        main(sys.argv[1])     