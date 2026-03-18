# AI Assignment – Dijkstra’s Algorithm on Indian Cities

## Problem Statement
Implement Dijkstra’s Algorithm (Uniform Cost Search) to compute the shortest path between cities in India using real-world road distances.

## Approach
- Cities are represented as nodes  
- Roads are represented as edges  
- Distance between cities is used as edge weight  
- Google Distance Matrix API is used to fetch real-world distances  
- A graph is constructed dynamically  
- Dijkstra’s Algorithm is applied to compute shortest paths  

## User Input
The program allows dynamic input:
- Number of cities  
- Names of cities  
- Starting city  

## Technologies Used
- Python  
- Google Distance Matrix API  
- VS Code  

## API Key Setup
Set your API key as an environment variable:

For Windows (PowerShell):

$env:GOOGLE_API_KEY="your_api_key"


Then run:

python main.py


## Requirements
Install dependencies:

pip install -r requirements.txt


## How to Run
1. Clone the repository  
2. Navigate to the folder  
3. Set API key  
4. Run the program  

## Sample Output

Delhi → Mumbai
Distance: 1400 km
Path: Delhi → Mumbai


## Features
- Uses real-world data  
- Implements Dijkstra’s Algorithm  
- Accepts user input  
- Efficient graph construction  

## Conclusion
This project demonstrates the application of Dijkstra’s Algorithm in solving real-world shortest path problems using live data.

## Q2: UGV Path Planning using A* Algorithm

- Implemented grid-based navigation
- Added obstacle generation with different densities (Low, Medium, High)
- Used A* algorithm for shortest path finding
- Avoids obstacles while navigating
- Measures of Effectiveness:
  - Path Length
  - Nodes Explored
  - Execution Time

  ---

## Q3: Path Planning with Dynamic Obstacles

In real-world environments, obstacles are not always static and may appear or move unpredictably. In such cases, the UGV must dynamically adapt its path.

A simple approach is to use A* algorithm repeatedly. Whenever a new obstacle is detected, the algorithm recomputes the path from the current position to the goal.

However, a more efficient approach is to use dynamic path planning algorithms such as D* (Dynamic A*) and D* Lite. These algorithms are specifically designed for environments where obstacles change over time. Instead of recomputing the entire path, they update only the affected parts of the path, making them faster and more efficient.

The working of the UGV in a dynamic environment is as follows:
1. Initialize the environment and compute an initial path
2. Move towards the goal step by step
3. Continuously sense the environment for new obstacles
4. If an obstacle is detected, update the map
5. Recompute or update the path using A* or D*
6. Continue until the goal is reached

Measures of Effectiveness include:
- Path length
- Number of nodes explored
- Time taken for replanning
- Number of replanning steps

Thus, dynamic path planning ensures that the UGV can safely and efficiently navigate even in uncertain and changing environments.