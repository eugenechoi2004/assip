import mercantile
import mapbox_vector_tile
import requests
import json
from vt2geojson.tools import vt_bytes_to_geojson

# define an empty geojson as output
output = {"type": "FeatureCollection", "features": []}

# Mapillary access token -- user should provide their own
access_token = 'MLY|5991746427532134|47846564489e8f482599a6175316d8c3'

# a bounding box in [east_lng,_south_lat,west_lng,north_lat] format
east, south, west, north = [-80.13423442840576,
                            25.77376933762778, -80.1264238357544, 25.788608487732198]
# get the tiles with x and y coors intersecting bbox at zoom 14 only
tiles = list(mercantile.tiles(east, south, west, north, 14))
print(tiles)
# loop through all tiles to get IDs of Mapillary data
for tile in tiles:
    tile_url = 'https://tiles.mapillary.com/maps/vtp/mly_map_feature_point/2/{}/{}/{}?access_token={}'.format(
        tile.z, tile.x, tile.y, access_token)
    response = requests.get(tile_url)
    data = vt_bytes_to_geojson(response.content, tile.x, tile.y, tile.z)
    print(data)
