#1usr/bin/python

import sys, getopt

class City:
  def __init__(self, name, minDistance = 99999999, visited = False):
    self.name = name  # Name of the city
    self.target = {}  # Creates the Target Dictionary holding cities to distance
    self.minDistance = minDistance #minumum distance to city initialized as the largest distance possible
    self.path = []  # Creates an empty Instance of a list for the path
    self.visit = False #Has the city been visited

  def AddTarget(self, city, distance): #adds to the target dictionary
    self.target[city] = distance;

  #Getter Functions
  def GetName(self):
    return self.name

  def GetTargets(self):
    return self.target;

  def GetDistance(self):
    return self.minDistance;

  def GetPath(self):
    return self.path;

  def GetTargetDistance(self, city):
    return self.target[city]

  def GetVisit(self):
    return self.visit;

  def HasVisited(self):
    self.visit = True;

  def MinCity(self, distance, path):  #Calculates the minimum distance to the city and replaces the path if necessary
    if (self.minDistance > distance):
       self.minDistance = distance;
       self.path = path
  
  def At(self, index):                        #Returns the value at the selected index along the path if the value is less than the size of the path array
    if (index > len(self.path) - 1): return "Error"
    else: return self.path[index]

def MakeGraph(input_file):                   #Converts inputfile into a graph
  Graph = {}
  
  try:
    with open(input_file, "rt") as file:     #Opens the file
      data = file.readlines()
      for line in data:
        words = line.split()  
        if (words[2]=="INPUT"):
            return Graph;
        elif (int(words[2]) < 0):
          print("Error, distance cannot be a negative value")
          exit(1)
        if words[0] not in Graph:                 #Checks if city is already in the graph
           Graph[words[0]] = City(words[0])
        if words[1] not in Graph:
          Graph[words[1]] = City(words[1])        #Checks if other city is in the graph
        x=Graph[words[0]]                         
        y=Graph[words[1]]
        try:                                      #Checks if the input is a valid integer instead of a string
          int(words[2])
        except ValueError:                        #Error in file format,
          print("3rd input  error, invalid format, now exiting.")
          exit(1)
        x.AddTarget(words[1],int(words[2]))        #adds the city as the target of the other, makes the linked list go both ways since a path may go back to a
 city.
        y.AddTarget(words[0],int(words[2]))
  except Exception as e:                          #Error in opening the file
    print(e)
    sys.exit(1)

def FindRoute(Graph):                                  #This function sets up the minimum distance & paths to every city with respect to the starting city
  dist = 99999999;	                               #Initialize a starting distance for the base case
  the_city = "";                                       #Initialize a starting psuedo city for the base case
  for i, v in Graph.items():
    if (v.GetVisit() == False) and (v.GetDistance() < dist):                        #If the city has not been visited
      dist = v.GetDistance();	                       #Update the distance
      the_city = v.GetName();                               #update the name of the city key
  if (dist == 99999999): return;                       #If there are no cities left, end
  Graph[the_city].HasVisited()                         #Update the city so I know I visited it
  x = Graph[the_city].target
  for i, v in (x.items()):  #Update the distances of every adjacent city if it is the minimum
    path = Graph[the_city].GetPath()                   #Track the path of the cities
    new_path=list(path)
    new_path.append(i)
    Graph[i].MinCity(dist + v, new_path) 
  FindRoute(Graph)                                     #Perform the function repeately until all cities have been visited
   
def main(argv):                                        #main function for running program, accepts 3 arguments
  if argv[1] is None:                                  #Ensures the appropriate number of arguments have been given.
    print("Missing 3 arguments, please try again.")
    exit(1)
  elif argv[2] is None:
    print("Missing 2 arguments, please try again.")
  elif argv[3] is None:
    print("Missing 1 argument, please try again.")
  input_file = argv[1];                                #Account for each of the given arguments
  start_city = argv[2];
  destination_city = argv[3];
  graph = MakeGraph(input_file)			       #processes my input file
  if start_city not in graph:                          #Checks if the city exists, quits if it does not.
     print("First city given is not in the Graph.\n No route available, now exiting")
     exit(1)
  elif destination_city not in graph:
     print("Second city is not in the graph.\n No route available, now exiting.")
     exit(1)
  graph[start_city].minDistance=0       			#Initialize the starting city with distance 0 and the path
  graph[start_city].path = [start_city]
  FindRoute(graph)                                     #runs my program with respect to the start city and graph
  if (start_city == destination_city):                 #If starting city is the same as my destination, print 0 and itself
    print('Distance: 0 km')
    print('route')
    print(start_city + " to " + destination_city + ', 0km')
  else:                                                #else 
    if (graph[destination_city].GetDistance() == 99999999): #If there is no path, print no path can be found
      print("Distance: Infinity")
      print("route: \nNone")
    else:
      print("Distance: " + str(graph[destination_city].GetDistance()) + " km")     #Else print each path of the cities along with the distance
      print("route:")
      for x in range(len(graph[destination_city].GetPath())):  #for each city in the path array
        first_city = graph[destination_city].At(x)             #retrieve the first city
        if (first_city != destination_city):                   #select the target of the second city unless first city is the end city
          second_city = graph[destination_city].At(x + 1)
          print(first_city + " to " + second_city + ", " + str(graph[first_city].GetTargetDistance(second_city)) + " km")

main(sys.argv)                                                 #Send given arguments to the main function
