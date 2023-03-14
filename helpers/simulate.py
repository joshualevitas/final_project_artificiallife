from Classes.simulation import SIMULATION

def simulate(directOrGUI,solutionID,links,joints,delete = True, gravity = "earth"):
    simulation = SIMULATION(directOrGUI,int(solutionID),links,joints,delete=delete, gravity="earth")
    if simulation == None: return 
    simulation.Run()
    simulation.Get_Fitness()