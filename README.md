# AI
## Activities and HW
<h3>Branch and bound</h3><br>
Algorithm that we are using to solve a TSP<br>
it works similar to backtracking and try to find the tour at the minium cost<br>
<Strong><h2>Graph</Strong></h2>

                  G.add_edge("A", "B")
                  G.add_edge("A", "C")
                  G.add_edge("A", "D")
                  G.add_edge("A", "E")
                  G.add_edge("B", "C")
                  G.add_edge("B", "D")
                  G.add_edge("B", "E")
                  G.add_edge("C", "D")
                  G.add_edge("C", "E")
                  G.add_edge("D", "E")
                  G.add_edge("E", "D")

 5 node graph  represented as a matrix<br>

                       [infinite, 20, 30, 10, 11],
                       [15, infinite, 16, 4, 2],
                       [3, 5, infinite, 2, 4],
                       [19, 6, 18, infinite, 3],
                       [16, 4, 7, 16, infinite],
   
                    
<Strong><h2>Redux</Strong></h2>
It is necessary to reduce the matrix according to the transfer that will be made, this is achieved by changing the values of the matrix of the participating nodes by infinity.
<br>
<Strong><h2>BnB</Strong></h2>
 it determinates if the matrix has been reduced, it is necessary to consult in each row and column if there is a value equal to 0 or infinity without taking into account the values of the route that is being followed<br>
With the new values in the columns and rows the value of b is determined<br>
b is a variable we got to use later.

