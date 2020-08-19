"""

class Hpfwh

                      ↓   inNode extracted steam(No.i)
                  ┌───┴───┐
 ourNode_fw       │       │
 feedwater      ← ┤       │← inNode_fw  feedwater(No.j)
     (No.l)       │       │
                  └───┬───┘
                      ↓   inNode_trap  trap water(No.k)

 json object example:

     {
            "name": "HP Feedwater Heater",
            "type": "HP-FWH",
            "inNode": i,
            "inNode_fw": j,
            "outNode_trap": k,
            "outNode_fw": l
     }

"""
from seuif97 import *
from .node import *


class Hpfwh:

    energy = 'internel'
    type = "HP-FWH"

    def __init__(self, dictDev, nodes):
        """
        Initializes the Closed heater
        """
        self.name = dictDev['name']
        self.inNode = dictDev['inNode']
        self.outNode_trap=dictDev['outNode_trap']
        self.inNode_fw = dictDev['inNode_fw']
        self.outNode_fw = dictDev['outNode_fw']

        self.iNode = nodes[self.inNode]
        self.oNode_trap = nodes[self.outNode_trap]
        self.iNode_fw = nodes[self.inNode_fw]
        self.oNode_fw = nodes[self.outNode_fw]

        self.heatAdded = 0
        self.heatExtracted = 0
        self.QAdded = 0
        self.QExtracted = 0

    def state(self):
        pass        

    def balance(self):
        
        """ mass and energy balance of the closed heater """

        # energy balance equation
        self.heatAdded = self.oNode_fw.fdot * \
            (self.oNode_fw.h - self.iNode_fw.h)

        self.heatExtracted = self.heatAdded

        self.iNode.fdot = self.heatExtracted / (self.iNode.h - self.oNode_trap.h)
        # mass balance equation
        self.iNode_fw.fdot = self.oNode_fw.fdot
        self.oNode_trap.fdot = self.iNode.fdot

        self.heatAdded = self.oNode_fw.fdot * \
            (self.oNode_fw.h - self.iNode_fw.h)
        self.heatExtracted = self.heatAdded

    def sm_energy(self):
        self.QExtracted = self.iNode.mdot * (self.iNode.h - self.oNode_trap.h)
        self.QExtracted /= (3600.0 * 1000.0)
        self.QAdded = self.QExtracted

    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode_trap.__str__()
        result += '\n' + self.iNode_fw.__str__()
        result += '\n' + self.oNode_fw.__str__()


        result += '\nheatAdded(kJ/kg) \t{:>.2f}'.format(self.heatAdded)
        result += '\nheatExtracted(kJ/kg) \t{:>.2f}'.format(self.heatExtracted)
        result += '\nQAdded(MW) \t{:>.2f}'.format(self.QAdded)
        result += '\nQExtracted(MW)  \t{:>.2f}'.format(self.QExtracted)

        return result