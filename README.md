# Bike Route to GPX Generator

This Python script allows you to generate bike route data and export it into GPX (GPS Exchange Format) files. The script is designed for cyclists looking to create detailed GPX files for use with GPS devices or route planning applications.

# Credits
Designed and Developed by Alex Tannenbaum, 2024.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Input Format](#input-format)
5. [Example](#example)
6. [GPX Output Format](#gpx-output-format)
7. [Dependencies](#dependencies)
8. [Contributing](#contributing)
9. [License](#license)

## Features

- Generate bike route data with start and end points.
- Export the route to a GPX file for use with GPS devices and applications.
- Customize route parameters such as waypoints, elevation, and segment breakdowns.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/StarShows/BikeRoute-Generator.git
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script:**

   ```bash
   python generate.py
   ```

2. **Arguments:**

   - `--input`: Specifies the input JSON file containing the route data (e.g., `/input/route_data.json`).
   - `--output`: Specifies the desired GPX file name for the generated route (e.g., `output_GPX/route_name.gpx`).

## Input Format

The input file should be a JSON file structured as follows:

```json
{
  "route_name": "Beautiful Coastal Ride",
  "description": "A scenic bike route along the coastline.",
  "coordinates": [
    {"lat": 34.012345, "lon": -118.495678, "elevation": 50},
    {"lat": 34.023456, "lon": -118.456789, "elevation": 100},
    ...
  ]
}
```

- `route_name`: Name of the bike route.
- `description`: Brief description of the route.
- `coordinates`: List of points (latitude, longitude, and elevation) that define the route.

## Example

To generate a GPX file from a sample route data:

1. Create a `route_data.json` file:

    ```json
    {
      "route_name": "Santa Monica to Malibu",
      "description": "A beautiful out-and-back ride along the Pacific Coast Highway.",
      "coordinates": [
        {"lat": 34.011856, "lon": -118.495338, "elevation": 15},
        {"lat": 34.020348, "lon": -118.490012, "elevation": 25},
        {"lat": 34.025324, "lon": -118.483294, "elevation": 35}
      ]
    }
    ```

2. Run the script:

    ```bash
    python generate.py --input route_data.json --output santa_monica_to_malibu.gpx
    ```

## GPX Output Format

The generated GPX file will include:

- Metadata with the route name and description.
- Track points (`<trkpt>`) with latitude, longitude, and elevation values.
- Optionally, waypoints and segments can be defined based on the input data.

## Dependencies

- `gpxpy`: A library for reading and writing GPX files.
- `argparse`: For handling command-line arguments.
- `json`: For parsing input JSON data.

Install these dependencies by running:

```bash
pip install -r requirements.txt
```

## Contributing

If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/my-new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/my-new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.