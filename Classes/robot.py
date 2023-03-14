import os 
import math
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

from Classes.sensor import SENSOR
from Classes.motor import MOTOR
from Classes.constants import Constants




class ROBOT:
    def __init__(self,solutionID,links, joints, delete=True) -> None:
        self.constants = Constants()
        self.solutionID = solutionID
        self.links = links
        self.joints = joints
        self.sensors = {}
        self.motors = {}
        try:
            self.robotId = p.loadURDF("body{}.urdf".format(solutionID))
        except:
            self.write_0_fitness()
            return None
        self.nn = NEURAL_NETWORK("brain{}.nndf".format(solutionID))
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_to_Act()
        if delete:
            pass
            os.system("rm brain{}.nndf".format(solutionID))
            os.system("rm body{}.urdf".format(solutionID))
        

    def Prepare_To_Sense(self):
        for linkName in self.links:
                self.sensors[linkName] = SENSOR(linkName)
    
    def Sense(self,t):
        for sensor in self.sensors:
            try:
                self.sensors[sensor].Get_Value(t)
            except:
                pass

    def Prepare_to_Act(self):
        for jointName in self.joints:
            try:
                self.motors[jointName] = MOTOR(jointName)
            except:
                pass

    def Act(self,t):
        try:
            for neuronName in self.nn.Get_Neuron_Names():
                if self.nn.Is_Motor_Neuron(neuronName):
                    jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                    desiredAngle = self.nn.Get_Value_Of(neuronName) * self.constants.motorJointRange
                    self.motors[jointName].Set_Value(self.robotId,desiredAngle)
        except:
            pass


    def Think(self):
        try:
            self.nn.Update()
        except:
            pass

    def Get_Fitness(self):
        try:
            basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
            basePosition = basePositionAndOrientation[0]
            xCoordinateOfLinkZero = basePosition[0]
            yCoord = basePosition[2]
            zCoord = basePosition[1]

            dist_squared = ((xCoordinateOfLinkZero - (0))**2 + (zCoord - (0))**2) # + (yCoord - (0))**2)
            dist = math.sqrt(dist_squared)
        except:
            dist = 0 
        with open("tmp{}.txt".format(self.solutionID), 'w') as f:
            f.write(str(dist))
        os.system("mv tmp{}.txt fitness{}.txt".format(self.solutionID,self.solutionID))
    
    def write_0_fitness(self):
        with open("tmp{}.txt".format(self.solutionID), 'w') as f:
            f.write(str('0.00'))
        os.system("mv tmp{}.txt fitness{}.txt".format(self.solutionID,self.solutionID))