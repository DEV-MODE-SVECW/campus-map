# SVECW Campus Navigator

A simple command-line application to find the shortest route and calculate the distance between two locations on the Shri Vishnu Engineering College for Women campus.

---

## What the Repo is About

The campus is modeled as a network of locations connected by paths with distances in meters.

When completed, the program will:
1. Show available campus locations.
2. Ask the user for a starting location and a destination.
3. Validate user inputs.
4. Calculate the shortest route and total distance.
5. Display the result clearly in the terminal.

---

## Current Status: What is Done and What is Pending

- **What is done**: The project structure and starter boilerplate are set up. Function definitions, imports, and file structures are ready in the `src/` directory.
- **What is pending**: The core logic inside all files is currently incomplete (`pass`). The team needs to implement the missing pieces across each module.

---

## Project Structure

```
campus-map/
├── .gitignore
├── README.md
└── src/
    ├── locations.py    # Campus locations data
    ├── routes.py       # Connections and path distances
    ├── navigator.py    # Shortest route algorithm
    ├── display.py      # Output formatting
    └── main.py         # Main program and input validation
```

---

## What is Missing & Actions Needed

### Campus Locations (`src/locations.py`)
- **Missing**: The list of campus landmarks is currently empty, and `get_locations()` returns nothing.
- **Action needed**:
  - Define `LOCATIONS` with campus places (you can choose which landmarks to include).
  - Implement `get_locations()` to return this list.

**Example format:**
```python
LOCATIONS = [
    "Main Gate",
    "Library",
    # Add more locations here...
]

def get_locations():
    return LOCATIONS
```

---

### Campus Connections (`src/routes.py`)
- **Missing**: `ROUTES` is currently an empty dictionary `{}`.
- **Action needed**:
  - Build the network map connecting locations and storing distances in meters using a dictionary of dictionaries.
  - Make sure connections are bidirectional: if location A connects to location B with distance D, then location B must also connect to location A with the same distance D.

**Example format:**
```python
ROUTES = {
    "Main Gate": {
        "CSE Block": 120,
        "Canteen": 180,
    },
    "CSE Block": {
        "Main Gate": 120,
        "Library": 80,
        # Add more connections...
    },
    # Add more locations...
}
```

---

### Route Finding (`src/navigator.py`)
- **Missing**: `find_shortest_route()` currently only has a `pass` placeholder.
- **Action needed**:
  - Given the routes dictionary, a source location, and a destination location, find the shortest path and return the path list along with the total distance.
  - Return a tuple: `(route_list, total_distance)`. If no route exists, return `([], 0)`.
  - You can use Dijkstra's Algorithm or Breadth-First Search (BFS).

**Example format:**
```python
# Input:
# routes = ROUTES
# source = "Main Gate"
# destination = "Library"

# Expected Output:
# (["Main Gate", "CSE Block", "Library"], 200)

def find_shortest_route(routes, source, destination):
    # Implement path finding logic
    pass
```

---

### Output & Display (`src/display.py`)
- **Missing**: `display_route()` does not yet print anything.
- **Action needed**:
  - Take the calculated route and distance, and format the output neatly so the user can easily read it in the terminal.

**Example format:**
```python
# Expected output on screen:
# Shortest route:
# Main Gate -> CSE Block -> Library
#
# Total distance: 200 m

def display_route(route, distance):
    # Format and print the route and distance
    pass
```

---

### Main Program Flow & Input Validation (`src/main.py`)
- **Missing**: The CLI interaction loop is not yet connected.
- **Action needed**:
  - Tie all the pieces together into a working interactive command-line application:
    1. Call `get_locations()` and print the available locations.
    2. Ask the user for their starting point and destination.
    3. Validate user input (check for invalid names, empty inputs, etc.).
    4. Call `find_shortest_route()` from the navigator module.
    5. Call `display_route()` from the display module to print the result.

---

## What Needs to Be Taken Care Of (Edge Cases)

When implementing the project, make sure the app handles these scenarios:
- **Valid route**: Returns the correct shortest path and distance.
- **Multiple possible routes**: Always picks the route with the smallest total distance, not just the first one found.
- **Invalid location**: If the user enters a place that does not exist, show a clear error message instead of crashing.
- **Same source and destination**: If source equals destination, handle it cleanly (e.g. 0 m distance).
- **No route available**: If two locations exist but there is no path connecting them, inform the user gracefully.

---

## How to Run the App

From the `campus-map` folder:

```bash
python src/main.py
```

### Example Interaction

```text
========================================
       SVECW CAMPUS NAVIGATOR
========================================

Available Locations:
- Main Gate
- CSE Block
- Library
- Canteen

Enter source: Main Gate
Enter destination: Library

Shortest route:
Main Gate -> CSE Block -> Library

Total distance: 200 m
```
