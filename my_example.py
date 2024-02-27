import dp_algorithm as dp
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import os

#clear command prompt
os.system('cls')

print("-----------This is my Cartographic Simplification tool based on the Douglas Peucker Algorithm-----------")

#GR_Coastline and rivers
#Read shapefiles
print("--------------------------------------Reading Coastline Shapefile---------------------------------------")
input_shapefile = "d:/Programming in Geoinformatics/project/in_shp/GR_Coastline.shp"
gdf = gpd.read_file(input_shapefile)

# Defining tolerance variable
tolerance = 1000000000000  # adjustable value

# Initializing list for simplified lines
simplified_lines = []

print("------------------------------------Simplifying Coastline Shapefile-------------------------------------")
# Simplifying all LineStrings in the Coastline GeoDataFrame
for index, row in gdf.iterrows():
    original_line = row['geometry']
    
    # Apply Douglas-Peucker to the LineString or list of coordinates
    simplified_line = dp.douglas_peucker(original_line, tolerance)
    simplified_lines.append(LineString(simplified_line))

# Create new GeoDataFrame with simplified lines
gdf_simplified = gpd.GeoDataFrame(geometry=simplified_lines)      
# Export simplified GeoDataFrames to new shapefiles
print("-------------------------------------Exporting Coastline Shapefile--------------------------------------")
gdf_simplified.to_file("d:/Programming in Geoinformatics/project/out_shp/Simplified_GR_Coastline.shp")
   
#Oria_line   
# Read shapefiles
print("---------------------------------------Reading Oria OTA Shapefile---------------------------------------")
input_shapefile2 = "d:/Programming in Geoinformatics/project/in_shp/Oria_line.shp"
gdf2 = gpd.read_file(input_shapefile2)

# Defining tolerance variable
tolerance2 = 1000000000000  # adjustable value

# Initializing list for simplified lines
simplified_lines2 = []

print("-------------------------------------Simplifying Oria OTA Shapefile-------------------------------------")
# Simplifying all LineStrings in the GeoDataFrame
for index, row in gdf2.iterrows():
    original_line2 = row['geometry']
    
    # Apply Douglas-Peucker to the LineString or MultiLineString geometry
    simplified_points2 = dp.douglas_peucker(original_line2, tolerance2)

    # Convert the simplified points back to a LineString
    simplified_line2 = LineString(simplified_points2)
    
    # Append the simplified LineString to the list
    simplified_lines2.append(simplified_line2)
    
# Create new GeoDataFrame with simplified lines
gdf_simplified2 = gpd.GeoDataFrame(geometry=simplified_lines2)    
# Export simplified GeoDataFrame to new shapefiles
print("--------------------------------------Exporting Oria OTA Shapefile--------------------------------------")
gdf_simplified2.to_file("d:/Programming in Geoinformatics/project/out_shp/Simplified_Oria_line.shp")

#Set dark background for the figures
plt.style.use('dark_background')

print("-------------------------------------------Plotting Coastline-------------------------------------------")
# Plot the original and simplified lines GR_Coastline
fig, ax = plt.subplots()

# Set the aspect ratio and axis to be equal
ax.set_aspect('equal')
ax.axis('equal')

# Lists to collect labels for legend
labels = []
labels2 = []

for original_line, simplified_line in zip(gdf['geometry'], simplified_lines):
    original_x, original_y = original_line.xy
    simplified_x, simplified_y = simplified_line.xy
    
    # Plot original and simplified lines
    original_handle, = ax.plot(original_x, original_y, color='xkcd:dodger blue', linewidth="1.2", linestyle="dashdot")
    simplified_handle, = ax.plot(simplified_x, simplified_y, color='xkcd:orange red', linewidth="1.2")
    
labels.extend(['Original Coast', 'Simplified Coast'])

# Create a single legend outside the loop
ax.legend(labels, loc='upper right')
# Display the figure without blocking
plt.show(block=False)

print("-------------------------------------------Plotting Oria OTA--------------------------------------------")
# Plot the original and simplified lines Oria_line
fig2, ax = plt.subplots()

# Set the aspect ratio and axis to be equal
ax.set_aspect('equal')
ax.axis('equal')

# List labels for legend
labels = []

for original_line2, simplified_line2 in zip(gdf2['geometry'], simplified_lines2):
    original_x2, original_y2 = original_line2.xy
    simplified_x2, simplified_y2 = simplified_line2.xy

    
    # Plot original and simplified lines
    original_handle2, = ax.plot(original_x2, original_y2, color='xkcd:kiwi green', linewidth="1.2", linestyle="dashdot",alpha=.75)
    simplified_handle2, = ax.plot(simplified_x2, simplified_y2, color='xkcd:shocking pink', linewidth="1.2",alpha=.9)
    
labels2.extend(['Original OTA', 'Simplified OTA'])

# Create a single legend outside the loop
ax.legend(labels2, loc='upper right')
# Display the figure without blocking
plt.show(block=False)

print("-------------------------------------------Example Completed--------------------------------------------")

#Keep figures open
plt.show()
