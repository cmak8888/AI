Calvin Mak
10728824

I used Python v3.6 for this program.

OS: Linux isengard 4.4.0-141-generic #167-Ubuntu SMP x86_64 x86_64 x86_64 GNU/Linux

How the code is structured:
The code uses one class called City. The city retains the name of a city, the adjacent "target" cities, the minimum distance to that city, and the shortest path to that city, and whether that city has been visited. The Graph is a dictionary from city name to the City class. The Graph is my overall "Graph" data structure holds all the information given by the input file. The MakeGraph method creates the Graph with the input file given. I have a lot of getter and setter functions since I was unfamiliar with python and separating class variables from instance variables. Within the City class, the two most important functions are MinCity and my At method. The MinCity compares the given distance to that with the current minimum distance. If the distance is smaller, it replaces the distance and the path with the smallest distance and the new shortest path. The At method looks basically looks into the Path List in the City. The adjacent "target" cities is also a dictionary with the key being the name of the adjacent city, and the value being the distance from the current city to the target(adjacent) city. This organizes data as a linked list from each city to each of its adjacent cities. The targets are added in both cities to form a doubly linked list since adjacent cities can go both ways. For the main algorithm itself I used Dijkstra's algorithm to compute my minimum distance and path. How it works is the algorithm looks through each node/city adjacent to the starting city. It updates all the distances to the adjacent cities from the current city incorporating the path to the current city. Then it marks the current city as visited. The next city chosen begins within the closest cit(ies) to the current city and adds it to the set of cities. The function is a recursive function with a new relative "starting city" with the path to that "starting city". The distance to each city is updated to maintain the shortest distance and the shortest path to each city. So the shortest path to every city from the starting city is pre-calculated. While it is a greedy algorithm, it assures that the shortest distance & path can be found given a list of cities and distances. Many other methods were added to ensure the most bugs and errors in syntax or input are accounted for. Any mistakes will usually cause the program to exit. 
The main function was added to Make the Graph and run the algorithm. In the end, it prints the output according to the prompt's given output.

Running the code:
The code must be ran through terminal/command prompt.
The code requires Python version 2.6 or 2.7.
To run the code, you simply need to cd into the directory.
The file is called find_route.py.
You may use the python or python3 command to run the code.
The code requires 3 arguments: inputfile, starting city and destination city.
Otherwise an error will be given and the program won't run.
Any errors in the file or the given arguments will result in a printed statement stating the error, and the program will immediately exit.
Line format:
python3 find_route.py <inputfile> <Starting city> <Destination City>
If the city is not given in the input file, it is setup to state that the city isn't valid and quit.

