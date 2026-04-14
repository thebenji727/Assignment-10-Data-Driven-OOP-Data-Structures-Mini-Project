import requests

class ApiClient:
    URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    def fetch(self):
        params = {
            "format": "geojson",
            "limit": 300,
            "orderby": "time",
            "minmagnitude": 3
        }
        return requests.get(self.URL, params=params).json()