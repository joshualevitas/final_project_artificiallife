import pickle
from parallelHillclimberUnpickled import PARALLEL_HILL_CLIMBER_UNPICKLED

def load_bot(path_to_bot):
    bot = open(path_to_bot, "rb")
    return pickle.load(bot)



# for i in range(5):
#     bot = load_bot("Data/MoonGravityCreature.json_" + str(i))
#     bot_phc = PARALLEL_HILL_CLIMBER_UNPICKLED(bot)
#     bot_phc.Show_Best()
#     input("press enter to continue") 
    

