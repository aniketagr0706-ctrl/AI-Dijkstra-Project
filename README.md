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