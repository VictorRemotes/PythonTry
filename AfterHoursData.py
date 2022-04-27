import datetime
import json
import os
import re

import loguru
import requests

class AfterHoursInfo:
    def __init__(
        self,
        code,
        name,
        totalShare,
        totalTurnover,
        openPrice,
        highestPrice,
        lowestPrice,
        closePrice
        ):
        
        self.Code = code        
        self.Name = name
        self.TotalShare = totalShare
        self.TotalTurnover = totalTurnover
        self.OpenPrice = openPrice
        self.HighesPrice = highestPrice
        self.LowestPrice = lowestPrice
        self.ClosePrice = closePrice
    
        
        