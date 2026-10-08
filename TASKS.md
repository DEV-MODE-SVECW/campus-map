# Campus Navigator — Task Sheet for Team of 5

This project is divided into 5 independent tasks, one for each student. 

## Phase 1 — Understand
Before coding:
1. Read the provided boilerplate code in all files.
2. Discuss the data structures (list for locations, graph/dict for routes) with your team.
3. Each student claims one file to complete.

---

## Required Tasks

### Student 1 — Campus Locations (`src/locations.py`)
- Maintain the list of campus locations.
- Define a list of strings for all places.
- Implement `get_locations()` to return this list.

### Student 2 — Campus Connections (`src/routes.py`)
- Represent which locations are connected and the distance between them.
- Use a nested dictionary representing a graph.
- Make sure the connections are bidirectional (if A connects to B, B connects to A).

### Student 3 — Route Finding (`src/navigator.py`)
- Given a source and destination, find a valid route.
- If multiple routes exist, return the route with the smallest total distance.
- You may want to research and implement **Dijkstra's Algorithm**.

### Student 4 — Display / Output (`src/display.py`)
- Format the final output neatly.
- Display the source, destination, route path (e.g., A -> B -> C), and total distance.

### Student 5 — Main Flow & Input Validation (`src/main.py`)
- Tie the modules together.
- Take user input for source and destination.
- Handle invalid source/destination inputs.
- Handle edge cases like source equal to destination or unreachable locations.

---

## Phase 2 — Integration & Testing
Once all modules are integrated, test the application with:
- a valid route
- an invalid location
- same source and destination

## Bonus
After all required tasks work:
- Add more campus locations.
- Add walking-time estimates.
- Add a "nearby locations" feature.
- Add a route summary.
