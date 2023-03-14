import time 

import pybullet as p
import pybullet_data
        
from Classes.constants import Constants
from Classes.world import WORLD
from Classes.robot import ROBOT




class SIMULATION:
    def __init__(self,directOrGUI,solutionID,links,joints,delete = True, gravity = "earth") -> None:
        self.constants = Constants()
        self.physicsClient = None 
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
            p.resetDebugVisualizerCamera(cameraDistance = 6, cameraYaw=30, cameraPitch=-40, cameraTargetPosition=[0,0,0])

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # if gravity == "moon":
        #     p.setGravity(0,0,-1.62)
        # elif gravity == "jupiter":
        #     p.setGravity(0,0,-24.79)
        # else:
        #     p.setGravity(0,0,-9.8)
        p.setGravity(0,0,-9.8)
        

        self.world = WORLD()
        print("World set up")
        self.robot = ROBOT(solutionID,links,joints,delete=delete)
        if self.robot == None: return None
        print("Simulation set up succesfully")

    def Run(self):
        print("running")
        for i in range(self.constants.num_steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(self.constants.sleep_time)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()