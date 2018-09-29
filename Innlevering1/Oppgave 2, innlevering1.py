#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:31:03 2018

@author: henrik
"""
from numpy import sqrt
import time
def manglerv(): #Regner ut farten
    E = float(input("Hvor stor er den kinetiske energien (oppgis i joule)? ")) 
    m = float(input("Hva er massen til objektet (oppgis i kilogram)? "))
    v = (E) / ( (1/2)*m)
    v = sqrt(v)
    print ("Farten til objektet er {:.2f}".format(v))
    time.sleep(4)


def manglerE(): #Regner ut den kinetiske energien
    v = float(input("Hvor fort beveger objektet seg? (oppgis i m/s)? "))
    m = float(input("Hva er massen til objektet (oppgis i kilogram)? "))
    E = (1/2)*(m)*(v**2)
    print ("Den kinetiske energien til objektet er {:.2f} joule.".format(E))
    time.sleep(4)


def manglerm(): #Regner ut massen til objektet
    E = float(input("Hvor stor er den kinetiske energien (oppgis i joule)? "))
    v = float(input("Hvor fort beveger objektet seg (oppgis i m/s)? "))
    m = (E) / ( (1/2)*v**2)
    print ("Massen til objektet er {:.2f} kg.".format(m))
    time.sleep(4)


def fysikkoppg(): #Ber brukeren velge hva hen vil regne ut, og sender deretter brukeren videre til funksjonen som trengs
    print ("Dette er en formel for kinetisk energi for et legme i bevegelse!")
    time.sleep(1)
    print ("Tast M, dersom du ønsker å finne MASSEN til objektet")
    time.sleep(1)
    print ("Tast V, dersom du ønsker å finne FARTEN til objektet")
    time.sleep(1)
    print ("Tast E, dersom du ønsker å finne den KINETISKE ENERGIEN til objektet")
    time.sleep(1)
    finn = input ("")
    if finn == 'M':
        manglerm() #Sender brukeren til funksjonen som vil regne ut massen til objektet
    elif finn == 'E':
        manglerE() #Sender brukeren til funksjonen som vil regne ut den kinetiske energien til objektet
    elif finn == 'V':
        manglerv() #Sender brukeren til funksjonen som vil regne ut objektets fart
        
fysikkoppg()