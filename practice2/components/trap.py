"""
 General Object-oriented Abstraction and JSON Textual Model of Rankine Cycle

  class  Condenser


 inNode trap water           ┌─────────┐   outNode trap water  
        (No.i)              →│         │→           (No.j)
                             └─────────┘
json object example:

   {
            "name": "Trap",
            "type": "TRAP",
            "inNode": i,
            "outNode": j
   },

"""

from seuif97 import *
from .node import *


class Trap:

    energy = "internel"
    type = "TRAP"

    def __init__(self, dictDev, nodes):
        """ Initializes the condenser """
        self.name = dictDev['name']
        self.inNode = dictDev['inNode']
        self.outNode = dictDev['outNode']
        self.iNode = nodes[self.inNode]
        self.oNode = nodes[self.outNode]

    def state(self):
        #self.iNode.h = px2h(self.iNode.p, self.iNode.x)
        #self.iNode.px()
        #self.oNode.h = self.iNode.h
        #self.oNode.ph()
        
        self.oNode.h = self.iNode.h
        self.oNode.ph()


    def balance(self):
        """ mass and energy balance of the condenser  """
        if (self.iNode.fdot != None):
            self.oNode.fdot = self.iNode.fdot
        elif (self.oNode.fdot != None):
            self.iNode.fdot = self.oNode.fdot

        '''self.heatExtracted = self.iNode.fdot * (self.iNode.h - self.oNode.h)'''

    def sm_energy(self):
        pass

    def __str__(self):
        result = '\n' + self.name
        result += '\n' + Node.title
        result += '\n' + self.iNode.__str__()
        result += '\n' + self.oNode.__str__()

        return result