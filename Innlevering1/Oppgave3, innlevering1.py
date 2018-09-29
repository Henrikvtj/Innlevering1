#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:22:02 2018

@author: henrik
"""

def biooppgave(): #Bruker prosentvis endring over perioder til å regne ut populasjonsendringen
    bgammel = int(input("Hvor mange dyr er det for tiden? ")) 
    t = int(input("Hvor mange år skjer populasjonsendringen over? "))
    pv = input("Stiger populasjonen? ja / nei ") 
    if pv == 'ja': #Regner ut populasjonsendringen dersom populasjonen stiger
        p = float(input("Hvor mange prosent stiger populasjonen? "))
        bny = (bgammel * (1 + (p/100))**t)
        print ("Det er {:.0f} dyr etter {} år.".format(bny, t))
    elif pv == 'nei': #Regner ut populasjonsendringen dersom populasjonen synker
        p = float(input("Hvor mange prosent synker populasjonen? "))
        bny = (bgammel * (1 - (p/100))**t)
        print ("Det er {:.0f} dyr etter {} år.".format(bny, t))
biooppgave()