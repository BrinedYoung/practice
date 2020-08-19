"""

class Lpfwh

                      ↓   inNode extracted steam(No.i)
                  ┌───┴───┐
 ourNode_fw       │       │
 feedwater      ← ┤       │← inNode_fw  feedwater(No.j)
     (No.l)       │       │
                  └───┬───┘
                      ↑   inNode_trap  trap water(No.k)

 json object example:

     {
            "name": "LP Feedwater Heater",
            "type": "LP-FWH",
            "inNode": i,
            "inNode_fw": j,
            "inNode_trap": k,
            "outNode_fw": l
     }

"""
from .node import *


class Lpfwh:

    energy = 'internel'
    type = "LP-FWH"

    def __init__(self, dictDev, nodes):
        """
        Initializes the Opened heater
        """
        self.name = dictDev['name']
        self.inNode = dictDev['inNode']
        self.inNode_trap=dictDev['inNode_trap']
        self.inNode_fw = dictDev['inNode_fw']
        self.outNode_fw = dictDev['outNode_fw']

        self.iNode = nodes[self.inNode]
        self.iNode_trap = nodes[self.inNode_trap]
        self.iNode_fw = nodes[self.inNode_fw]
        self.oNode_fw = nodes[self.outNode_fw]

        self.heatAdded = 0
        self.heatExtracted = 0
        self.heatExtracted_s = 0
        self.heatExtracted_d = 0
        self.QExtracted = 0
        self.QExtracted_s = 0
        self.QExtracted_d = 0

    def state(self):
        pass        

    def balance(self):

        """ mass and energy balance of the opened heater """

        # energy balance equation
        self.heatAdded = self.oNode_fw.fdot * \
            (self.oNode_fw.h - self.iNode_fw.h)

        self.heatExtracted = self.heatAdded

        self.iNode.fdot = ((1 - self.iNode_trap.fdot) * self.iNode_fw.h + self.iNode_trap.fdot * \
            self.iNode_trap.h - self.oNode_fw.h) / (self.iNode_fw.h - self.iNode.h)
        # mass balance equation
        self.iNode_fw.fdot = self.oNode_fw.fdot - self.iNode.fdot - self.iNode_trap.fdot

        self.heatAdded = self.oNode_fw.fdot * \
            (self.oNode_fw.h - self.iNode_fw.h)
        self.heatExtracted = self.heatAdded
        self.heatExtracted_s = self.iNode.fdot * (self.iNode.h - self.iNode_fw.h)
        self.heatExtracted_d = self.iNode_trap.fdot * (self.iNode_trap.h - self.iNode_fw.h)

    def sm_energy(self):
        self.QExtracted_s = self.iNode.mdot * (self.iNode.h - self.oNode_fw.h)
        self.QExtracted_d = self.iNode_trap.mdot * (self.iNode_trap.h - self.oNode_fw.h)
        self.QExtracted = self.iNode.mdot * (self.iNode.h - self.oNode_fw.h) + self.iNode_trap.mdot * \
            (self.iNode_trap.h - self.oNode_fw.h)
        self.QExtracted /= (3600.0 * 1000.0)
        self.QExtracted_s /= (3600.0 * 1000.0)
        self.QExtracted_d /= (3600.0 * 1000.0)
        self.QAdded = self.QExtracted

    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.iNode_fw.__str__()
        result += '\n' + self.oNode_fw.__str__()
        result += '\n' + self.iNode_trap.__str__()

        result += '\nheatAdded(kJ/kg) \t{:>.2f}'.format(self.heatAdded)
        result += '\nheatExtracted(kJ/kg) \t{:>.2f}'.format(self.heatExtracted)
        result += '\n heatExtracted_s(kJ/kg)\t{:>.2f}'.format(self.heatExtracted_s)
        result += '\n heatExtracted_d(kJ/kg)\t{:>.2f}'.format(self.heatExtracted_d)    
        result += '\nQAdded(MW) \t{:>.2f}'.format(self.QAdded)
        result += '\nQExtracted(MW)  \t{:>.2f}'.format(self.QExtracted)
        result += '\nQExtracted_s(MW)\t{:>.2f}'.format(self.QExtracted_s)
        result += '\nQExtracted_d(MW)\t{:>.2f}'.format(self.QExtracted_d)
        return result