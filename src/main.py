"""
Main Application & Input Validation

Tie all modules together to run the campus navigator:
1. Get the list of locations and print them.
2. Ask the user for a source and destination.
3. Validate user input (e.g. check if locations exist, source is not destination).
4. Call find_shortest_route() from navigator.
5. Call display_route() to show the result.
"""

from locations import get_locations
from routes import ROUTES
from navigator import find_shortest_route
from display import display_route


def main():
    print("========================================")
    print("       SVECW CAMPUS NAVIGATOR")
    print("========================================")

    # TODO: 1. Get locations from get_locations()
    
    # TODO: 2. Print available locations
    
    # TODO: 3. Ask the user for 'source' and 'destination'
    
    # TODO: 4. Add Input Validation 
    # (e.g., handle invalid location, source == destination)

    # TODO: 5. Call find_shortest_route(ROUTES, source, destination)
    
    # TODO: 6. Call display_route(route, distance)
    pass


if __name__ == "__main__":
    main()


