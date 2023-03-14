# from Old.parallelHillclimber import PARALLEL_HILL_CLIMBER
from Classes.parallelHillclimber_RandomBodies import PARALLEL_HILL_CLIMBER_RANDOM_BODY
from parallelHillclimberUnpickled import PARALLEL_HILL_CLIMBER_UNPICKLED
# from Old.solution import SOLUTION
from Classes.random_solution import RANDOM_SOLUTION

# def evolve():
#     phc = PARALLEL_HILL_CLIMBER()
#     phc.Evolve()
#     phc.Show_Best()

# def random():
#     r = SOLUTION(0)
#     r.Evaluate("DIRECT")


def random_unevolved():
    r = RANDOM_SOLUTION(0)
    r.Evaluate("DIRECT")

def random_evolved(show=True,seed = None):
    phc = PARALLEL_HILL_CLIMBER_RANDOM_BODY(seed = seed)
    phc.Evolve()
    if show:
        phc.Show_Best()
    return phc.fitness_vals

def random_evolved_to_pickle(seed = None):
    phc = PARALLEL_HILL_CLIMBER_RANDOM_BODY(seed = seed)
    phc.Evolve()
    return phc.get_best_to_pickle()

def random_evolved_from_pickle(seed = None, show = True):
    # seed.Recreate_Body()
    # seed.Create_Brain()
    # print("got here")
    phc = PARALLEL_HILL_CLIMBER_UNPICKLED(seed = seed)
    # print("\n\n phc initialized \n\n")
    phc.Evolve()
    print("\n\n evolved creature \n\n")
    if show:
        phc.Show_Best()
    

    return phc.fitness_vals, phc.get_best_to_pickle()