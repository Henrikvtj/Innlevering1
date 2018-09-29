#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:20:16 2018

@author: henrik
"""
import math
def kjemioppg():
    ioner = float(input("Hvor mange ioner per mol er det i løsingen din? "))

    pH = -math.log(ioner) #Lager en variabel som skal regne ut pH verdien

    if 0 <= pH < 7: #Sjekker om pH verdien er basisk, nøytral eller sur:
        print ("Løsningen er sur")
    elif pH == 7:
        print ("Løsningen er nøytralt")
    else:
        print ("Løsningen er basisk")
kjemioppg()