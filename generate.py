import gpxpy.gpx
import os
import re

# Prompt the user for route name and description
route_name = input("Enter the route name: ")
description = input("Enter the route description: ")

# Initialize an empty list for coordinates
coordinates = []

# Keep asking for coordinates until "end" is detected
while True:
    lat = input("Enter latitude (or type 'end' to finish): ")
    if lat.lower() == 'end':
        break
    lon = input("Enter longitude: ")
    elevation = input("Enter elevation: ")

    # Confirm the entered values
    confirm = input(f"Confirm coordinates (lat: {lat}, lon: {lon}, elevation: {elevation})? (yes/no): ").lower()
    if confirm == 'no':
        lat = input("Re-enter latitude: ")
        lon = input("Re-enter longitude: ")
        elevation = input("Re-enter elevation: ")

    coordinates.append((float(lat), float(lon), float(elevation)))

# Create GPX track and segment
gpx = gpxpy.gpx.GPX()
gpx_track = gpxpy.gpx.GPXTrack(name=route_name, description=description)
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Add points to the segment
for coord in coordinates:
    point = gpxpy.gpx.GPXTrackPoint(coord[0], coord[1], elevation=coord[2])
    gpx_segment.points.append(point)

# Write the GPX file to disk
output_dir = "Output_GPX"
os.makedirs(output_dir, exist_ok=True)

# Convert route name to snake_case for the file name
def to_snake_case(name):
    name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    name = re.sub(r'\s+', '_', name)
    return name.lower()

file_name = to_snake_case(route_name) + ".gpx"
file_path = os.path.join(output_dir, file_name)

with open(file_path, 'w') as f:
    f.write(gpx.to_xml())

print(f"GPX file saved to {file_path}")