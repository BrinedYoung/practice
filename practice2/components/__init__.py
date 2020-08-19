"""
 General Object-oriented Abstraction and JSON Textual Representation of Rankine Cycle 
   
    Components Package of the General Simulator of Rankine Cycle 
"""

from .node import Node

from .boiler import Boiler
from .turbineex0 import TurbineEx0
from .turbineex1 import TurbineEx1
from .turbine86 import Turbine86
from .reheater import Reheater
from .condenser import Condenser
from .pump import Pump
from .lpfwh import Lpfwh
from .hpfwh import Hpfwh
from .openedheaterdw0 import OpenedheaterDw0
from .trap import Trap


# ------------------------------------------------------------------------------
# compdict(jump table)
#  1: key:value-> Type String: class  name
#  2    add the new key:value to the dict after you add the new device class/type
# --------------------------------------------------------------------------------

compdict = {
    "BOILER": Boiler,
    "TURBINE-EX1": TurbineEx1,
    "TURBINE-EX0": TurbineEx0,
    "TURBINE-86": Turbine86,
    "REHEATER": Reheater,
    "CONDENSER": Condenser,
    "HP-FWH": Hpfwh,
    "LP-FWH": Lpfwh,
    "PUMP": Pump,
    "FWH-OPEN-DW0": OpenedheaterDw0,
    "TRAP": Trap    
}
