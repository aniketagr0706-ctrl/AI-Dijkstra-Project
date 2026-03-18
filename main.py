import requests
import heapq
import json
import os
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("Error: API key not found. Set GOOGLE_API_KEY.")
    exit()
def get_user_cities():
    n = int(input("Enter number of cities: "))
    cities = []
    for i in range(n):
        city = input(f"Enter city {i+1}: ")
        cities.append(city)
    return cities
def get_distance_matrix(origins, destinations):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": "|".join(origins),
        "destinations": "|".join(destinations),
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data["status"] != "OK":
        print("API Error:", data)
        return None
    return data
def build_graph(cities):
    graph = {city: {} for city in cities}
    print("Fetching distances from API...")
    data = get_distance_matrix(cities, cities)
    if data is None:
        return None
    for i, origin in enumerate(cities):
        for j, destination in enumerate(cities):
            if origin != destination:
                element = data["rows"][i]["elements"][j]
                if element["status"] == "OK":
                    graph[origin][destination] = element["distance"]["value"]
                else:
                    graph[origin][destination] = float('inf')
    with open("graph_data.json", "w") as f:
        json.dump(graph, f, indent=4)
    print("Graph saved locally!")
    return graph
def load_graph():
    if os.path.exists("graph_data.json"):
        with open("graph_data.json", "r") as f:
            print("Loaded graph from file!")
            return json.load(f)
    return None
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous
def get_path(previous, start, end):
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path if path[0] == start else []
if __name__ == "__main__":
    cities = get_user_cities()
    start_city = input("Enter starting city: ")
    graph = load_graph()
    if graph is None:
        graph = build_graph(cities)
    if graph is None:
        print("Error building graph.")
        exit()
    print(f"\nShortest paths from {start_city}:\n")
    distances, previous = dijkstra(graph, start_city)
    for city in cities:
        if city == start_city:
            continue
        path = get_path(previous, start_city, city)
        distance_km = distances[city] / 1000
        print(f"{start_city} → {city}")
        print(f"Distance: {distance_km:.2f} km")
        print(f"Path: {' → '.join(path)}\n")