
"""
 
  class  Reheater


 inNode exhausted steam      ┌─────────┐   outNode reheat steam  
        (No.i)              →│         │→           (No.j)
                             └─────────┘
             
json object example:

   {
            "name": "Reheater",
            "type": "REHEATER",
            "inNode": i,
            "outNode": j
   },

"""

from seuif97 import *
from .node import *


class Reheater:

    energy = "heatAdded"
    type = "REHEATER"

    def __init__(self, dictDev, nodes):
        """
        Initializes the reheater
        """
        # self.__dict__.update(dictDev)

        self.name = dictDev['name']
        self.inNode = dictDev['inNode']
        self.outNode = dictDev['outNode']
        self.iNode = nodes[self.inNode]
        self.oNode = nodes[self.outNode]

        self.heatAdded = 0

    def state(self):
        pass

    def balance(self):
        """ 
        mass and energy balance of the boiler
        """
        # mass blance equation
        if (self.iNode.fdot != None):
            self.oNode.fdot = self.iNode.fdot
        elif (self.oNode.fdot != None):
            self.iNode.fdot = self.oNode.fdot

        self.heatAdded = self.iNode.fdot * (self.oNode.h - self.iNode.h)

    def sm_energy(self):
        self.QAdded = self.iNode.mdot * \
            (self.oNode.h - self.iNode.h)
        self.QAdded /= (3600.0 * 1000.0)

    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode.__str__()
        result += '\nheatAdded(kJ/kg) \t{:>.2f} \nQAdded(MW) \t{:>.2f}'.format(
            self.heatAdded, self.QAdded)
        return result