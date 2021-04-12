# -*- coding: utf-8 -*-

import pandas as pd

air_quality = pd.read_csv("../air_quality_no2_long.csv")
print(air_quality)

# quick visual check of the data
air_quality.plot()
"""
Figures now render in the Plots pane by default. 
To make them also appear inline in the Console, 
uncheck "Mute Inline Plotting" under the Plots pane options menu. 
"""
