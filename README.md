# Borehole Access

UNHCR has the primary responsibility for coordinating, drafting, updating and promoting guidance related to water, sanitation and hygiene (WASH) in refugee settings.

We were for the first time able to collect extensive geolocation data for a number of African refugee camps, down to individual tents. In addition, UNHCR WASH provides borehole data with detailed information about the properties, location and safe yield of the boreholes that provide water supply to millions of refugees.

Water access is a basic human right, and is essential to the life, health, and dignity of refugee populations. Using UNHCR WASH standards as guidance, the borehole and geolocation data can be combined to provide effective visualizations that illustrate the quality of water access. UNHCR WASH already provides a basic exploration tool (http://wash.unhcr.org/wash-gis-portal) for the borehole data. Map overlays might be created that illustrate how well populations are currently served in terms of the safe supply of water provided by boreholes within some spatial distance. Where are populations most at risk in case a pump fails, and in what locations would new boreholes make the biggest difference to people? Are there ways of connecting the experience of refugees to people in other countries, that might help underline the hardship in camps (i.e., until where would someone have to walk from their house in California if they had to rely on boreholes for water access?). 

The tools you build, and the insights you glean, can both help UNHCR make a difference on the ground, and raise awareness for the refugee crisis.

The `Data Summary` notebook contains a rough overview of the datasets, along with some utility functions that you may find helpful (for example to calculate geographical distances based on longitude and latitude). The `UNHCR_data` subfolder contains raw data. The coverage of the borehole data and the tent geolocation data does not necessarily overlap. An additional file, `filtered_geolocation_data.json`, only contains entries for tents that are within 50km of a borehole. The function that generated this dataset is at the end of the `Data Summary` notebook. Note that the function may take a while to run. 

## UNHCR WASH Resources
http://wash.unhcr.org/

### Emergency Water Standard
https://emergency.unhcr.org/entry/248763/emergency-water-standard

### WASH Manual
http://wash.unhcr.org/unhcr-wash-manual-for-refugee-settings/


## Datasets

### UNHCR WASH Borehole Data
A csv file can be downloaded here: http://wash.unhcr.org/wash-gis-portal/. It is also in the `UNHCR_data` folder.

### Refugee Camp Geolocation Data
Contained in the `UNHCR_data` subfolder. Note that camp and borehole datasets do not perfectly overlap, and that it will be necessary to identify for which camps both geolocation and borehole data is present. 

### General Purpose Satellite Imagery
GBDX (https://platform.digitalglobe.com/gbdx/) provides vast amounts of sattelite imagery.
