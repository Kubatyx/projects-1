from ortools.linear_solver import pywraplp
from ortools.sat.python import cp_model
from pathlib import Path

# milp wykorzystywany do latwiejszych problemów, c

class RPQ() :
    def __init__ (self, r, p, q ) :
        self.R = r
        self.P = p
        self.Q = q
def Milp( jobs , instanceName ) : #mixed-integer linear programming, odpowiednie zapisanie ograniczen
    variablesMaxValue = 0
    for i in range (len(jobs)): # wartosc maksymalna
        variablesMaxValue += ( jobs[i].R+jobs[i].P+jobs[i].Q)
    solver = pywraplp.Solver('simple_mip_program',pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    #variables :
    alfasMatrix = {} #attention! dictionary - not list! macierz

    for i in range (len(jobs)):
        for j in range (len(jobs)):
            alfasMatrix [i,j] = solver.IntVar(0,1," alfa "+str(i)+"_"+str(j))
    starts = [] #rozpoczecie poszczegolnych zadan
    for i in range ( len ( jobs ) ) :
        starts.append(solver.IntVar(0,variablesMaxValue,"starts"+str(i)))
    cmax = solver . IntVar (0 , variablesMaxValue , "cmax" )

    # ograniczenia:
    for i in range ( len ( jobs ) ) :
        solver.Add(starts[i]>=jobs[i].R) # start wiekszy od przygotowania
        solver.Add(cmax>= starts [ i ] + jobs [ i ] . P+jobs [ i ] .Q)
    # kolejnosc wykonwywania zadan
    for i in range ( len ( jobs ) ) :
        for j in range ( i +1 ,len ( jobs ) ) :
            solver.Add( starts[i]+jobs[i].P<=starts[j]+ alfasMatrix [i,j]*variablesMaxValue )
            solver.Add( starts[j]+jobs[j].P<=starts[i]+ alfasMatrix [j,i]*variablesMaxValue )
            solver.Add( alfasMatrix [ i , j ] + alfasMatrix [ j , i ] == 1)
    # solver:
    solver.Minimize(cmax)
    status = solver.Solve()
    if(status is not pywraplp.Solver.OPTIMAL) :
        print ( "Not optimal ! " )
    print (instanceName , "Cmax: " , solver.Objective( ).Value( ))
    pi = [ ]
    for i in range ( len(starts) ) :
        pi.append(( i, starts[i].solution_value ( ) ) )
    pi.sort(key=lambda x : x [ 1 ])
    print (pi)


def GetRPQsFromFile( pathToFile ) :
    fullTextFromFile = Path( pathToFile ) . read_text ()
    words = fullTextFromFile.replace("\n"," ").split(" ")
    words_cleaned = list(filter(None, words ))
    numbers = list(map( int , words_cleaned ))
    
    numberOfJobs = numbers[0]
    numbers.pop(0)
    numbers.pop(0)
    jobs = [ ]
    for i in range (numberOfJobs ) :
        jobs.append(RPQ(numbers[0], numbers[1], numbers[2]) )
        numbers.pop(0)
        numbers.pop(0)
        numbers.pop(0)
    return jobs

def CP(jobs, instanceName) :
    variablesMaxValue = 0
    for i in range (len(jobs)):
        variablesMaxValue += ( jobs[i].R+jobs[i].P+jobs[i].Q)
    
    #solver = pywraplp.Solver('simple_mip_program',pywraplp . Solver .CBC_MIXED_INTEGER_PROGRAMMING)
    #variables  
    solver = cp_model.CpModel()

    alfasMatrix = {} #attention! dictionary - not list!

    for i in range (len(jobs)):
        for j in range (len(jobs)):
            alfasMatrix [i,j] = solver.NewIntVar(0,1," alfa "+str(i)+"_"+str(j)) #NewIntVar dla problemu cp
    starts = []
    for i in range ( len ( jobs ) ) :
        starts.append(solver.NewIntVar(0,variablesMaxValue,"starts"+str(i))) #NewIntVar
    cmax = solver . NewIntVar (0 , variablesMaxValue , "cmax" ) #NewIntVar

    # constraints/ograniczenia:
    for i in range ( len ( jobs ) ) :
        solver.Add(starts[i]>=jobs[i].R)
        solver.Add(cmax>= starts [ i ] + jobs [ i ] . P+jobs [ i ] .Q)
    for i in range ( len ( jobs ) ) :
        
        for j in range ( i +1 ,len ( jobs ) ) :
            solver.Add( starts[i]+jobs[i].P<=starts[j]+ alfasMatrix [i,j]*variablesMaxValue )
            solver.Add( starts[j]+jobs[j].P<=starts[i]+ alfasMatrix [j,i]*variablesMaxValue )
            solver.Add( alfasMatrix [ i , j ] + alfasMatrix [ j , i ] == 1)

    # solver
    solver.Minimize(cmax)

    model = solver
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status is not cp_model.OPTIMAL:
        print("Not OPTIMAL !!!")
    print(instanceName, "Cmax CP:", solver.ObjectiveValue())
    pi = []
    for i in range(len(starts)):
        pi.append((i,solver.Value(starts[i])))
    pi.sort(key=lambda x:x[1])
    print (pi)
    #print(pi)



print("data0 4 RPQ")
file_paths = [ "data.000.txt"]
for i in range ( len ( file_paths) ) :
    jobs = GetRPQsFromFile(file_paths[i])
    #Milp( jobs , file_paths[i])
    CP( jobs, file_paths[i])

