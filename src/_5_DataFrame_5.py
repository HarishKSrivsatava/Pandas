import pandas as pd

air_quality = pd.read_csv("../air_quality_no2_long.csv")

print(air_quality.head(6))

"""
    city country                   date.utc location parameter  value   unit
0  Paris      FR  2019-06-21 00:00:00+00:00  FR04014       no2   20.0  µg/m³
1  Paris      FR  2019-06-20 23:00:00+00:00  FR04014       no2   21.8  µg/m³
2  Paris      FR  2019-06-20 22:00:00+00:00  FR04014       no2   26.5  µg/m³
3  Paris      FR  2019-06-20 21:00:00+00:00  FR04014       no2   24.9  µg/m³
4  Paris      FR  2019-06-20 20:00:00+00:00  FR04014       no2   21.4  µg/m³
5  Paris      FR  2019-06-20 19:00:00+00:00  FR04014       no2   25.3  µg/m³
"""

# derived column
air_quality["newCoulmn"] = air_quality["value"]*2
print(air_quality.head(6))
"""
    city country                   date.utc  ... value   unit  newCoulmn
0  Paris      FR  2019-06-21 00:00:00+00:00  ...  20.0  µg/m³       40.0
1  Paris      FR  2019-06-20 23:00:00+00:00  ...  21.8  µg/m³       43.6
2  Paris      FR  2019-06-20 22:00:00+00:00  ...  26.5  µg/m³       53.0
3  Paris      FR  2019-06-20 21:00:00+00:00  ...  24.9  µg/m³       49.8
4  Paris      FR  2019-06-20 20:00:00+00:00  ...  21.4  µg/m³       42.8
5  Paris      FR  2019-06-20 19:00:00+00:00  ...  25.3  µg/m³       50.6
"""
