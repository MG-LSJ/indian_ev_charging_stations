from typing import TypedDict
import json, geojson


# typed dictionary for locations
class Location(TypedDict):
    address: str
    city: str
    availability: int
    contact: str
    isValidated: str
    issue: int
    lattitude: str
    longitude: str
    name: str
    notes: str
    phones: str
    pincode: str
    pricing: str
    state: str
    stationid: str
    type: str


features = []

with open("data.json", "r") as f:
    data: list[Location] = json.load(f)
    for places in data:
        try:
            features.append(
                geojson.Feature(
                    geometry=geojson.Point(
                        (float(places["longitude"]), float(places["lattitude"]))
                    ),
                    properties=places,
                )
            )
        except ValueError:
            print("Error parsing location")
            print(places)
            print("Skipping...")

with open("ev_charging_stations.geojson", "w") as f:
    geojson.dump(geojson.FeatureCollection(features), f)

print("\n\nDone!")
