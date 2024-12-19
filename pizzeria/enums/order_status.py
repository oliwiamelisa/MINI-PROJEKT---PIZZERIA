from dataclasses import dataclass
from enum import Enum, auto

class OrderStatus(Enum):
    NOT_CONFIRMED = auto() 
    CONFIRMED = auto()
    CANCELLED = auto()
    DELIVERY = auto()
    FINISHED = auto()