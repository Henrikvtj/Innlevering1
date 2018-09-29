#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 14:22:41 2018

@author: henrik
"""

def matte():
    n = float(input("Skriv inn n-fakultetet: ")) #Ber brukeren skrive inn n-fakultet
    if n%1 != 0 or n < 0: #Sjekker om nummeret er et heltall
        print ("Ikke gyldig nummer.")
    else: 
        def VanskeligR1Matte(n): #Regner ut n-fakultetet dersom tallet er et heltall
            if n == 0:
                return 1
            else:
                return n * VanskeligR1Matte(n-1)
        print ("Svaret er {0}!".format(VanskeligR1Matte(n))) #Printer n-fakultetet
matte()