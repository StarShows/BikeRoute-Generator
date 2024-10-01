import gpxpy
import gpxpy.gpx

# Create a new GPX file
gpx = gpxpy.gpx.GPX()

# Define the coordinates for the Great Western Loop
# Coordinates are approximate and simplified for key points.

# Add the starting point at Lyons Valley Trading Post
start = gpxpy.gpx.GPXTrackPoint(32.7087, -116.7645, name="Start: Lyons Valley Trading Post (Parking)")
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)
gpx_segment.points.append(start)

# Add mid-route rest stop at Dehesa Rd
rest_stop_1 = gpxpy.gpx.GPXTrackPoint(32.8083, -116.7755, name="Rest Stop: Dehesa Rd")
gpx_segment.points.append(rest_stop_1)

# Add second rest stop at Japatul Valley Rd
rest_stop_2 = gpxpy.gpx.GPXTrackPoint(32.8146, -116.6987, name="Rest Stop: Japatul Valley Rd")
gpx_segment.points.append(rest_stop_2)

# Add the end point back to Lyons Valley Trading Post to complete the loop
end = gpxpy.gpx.GPXTrackPoint(32.7087, -116.7645, name="End: Lyons Valley Trading Post (Parking)")
gpx_segment.points.append(end)

# Write the GPX file to disk
with open("great_western_loop_fixed.gpx", "w") as f:
    f.write(gpx.to_xml())

print("GPX file created successfully.")
