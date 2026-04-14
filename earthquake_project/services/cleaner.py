from datetime import datetime

class Cleaner:
    def clean(self, raw_features):
        cleaned = []

        for item in raw_features:
            props = item["properties"]
            if props["mag"] is None:
                continue

            cleaned.append(
                Record(
                    datetime.fromtimestamp(props["time"] / 1000),
                    float(props["mag"]),
                    props["place"]
                )
            )

        return cleaned