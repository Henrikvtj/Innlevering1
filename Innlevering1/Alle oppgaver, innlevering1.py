'''Innlevering ProgMod
    Henrik von Tangen-Jordan 
        Uke 39
          '''
          
          
'''I dette programmet er alle innleveringsoppgavene satt inn i ett og samme program
        dette gjør at jeg kan bruke en startfunksjon til å dirigere brukeren til
            den funksjonen / oppgaven hen ønsker å bruke / innspisere.
                                                                            '''

import math   #Importerer biblioteket som behøves for å bruke logaritmer
from numpy import sqrt

#-----------------------------------------------------------------------------Oppgave. 1

def kjemioppg():
    ioner = float(input("Hvor mange ioner per mol er det i løsingen din? "))

    pH = -math.log(ioner) #Lager en variabel som skal regne ut pH verdien

    if 0 <= pH < 7: #Sjekker om pH verdien er basisk, nøytral eller sur:
        print ("Løsningen er sur")
    elif pH == 7:
        print ("Løsningen er nøytralt")
    else:
        print ("Løsningen er basisk")
    time.sleep(3)
    startfunksjon()

#-----------------------------------------------------------------------------Oppgave. 2

import time
def manglerv(): #Regner ut farten
    E = float(input("Hvor stor er den kinetiske energien (oppgis i joule)? ")) 
    m = float(input("Hva er massen til objektet (oppgis i kilogram)? "))
    v = (E) / ( (1/2)*m)
    v = sqrt(v)
    print ("Farten til objektet er {:.2f}".format(v))
    time.sleep(4)
    startfunksjon()

def manglerE(): #Regner ut den kinetiske energien
    v = float(input("Hvor fort beveger objektet seg? (oppgis i m/s)? "))
    m = float(input("Hva er massen til objektet (oppgis i kilogram)? "))
    E = (1/2)*(m)*(v**2)
    print ("Den kinetiske energien til objektet er {:.2f} joule.".format(E))
    time.sleep(4)
    startfunksjon()

def manglerm(): #Regner ut massen til objektet
    E = float(input("Hvor stor er den kinetiske energien (oppgis i joule)? "))
    v = float(input("Hvor fort beveger objektet seg (oppgis i m/s)? "))
    m = (E) / ( (1/2)*v**2)
    print ("Massen til objektet er {:.2f} kg.".format(m))
    time.sleep(4)
    startfunksjon()

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
    else:
        print ("Ikke gyldig alternativ! \n")
        time.sleep(1.5)
        print ("Restarting... \n")
        time.sleep(4)
        startfunksjon()

#-----------------------------------------------------------------------------Oppgave. 3

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
    else:
        print ("Ikke gyldig svar.")
    time.sleep(4)
    startfunksjon()

#-----------------------------------------------------------------------------Oppgave. 4

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
    time.sleep(4)
    startfunksjon()

#-----------------------------------------------------------------------------Startfunksjon

def startfunksjon(): #Startfunksjon som vil sende brukeren til den ønskede oppgaven / funksjonen
    print ("\nHva ønsker du å regne ut? \n1. pHen i en løsning utfra ioner i en løsning, \n2. formel for kinetisk energi for et legme i bevegelse,\n3. Antall tøffeldyr etter x år,\n4. n-fakultet,\n5. Exit")
    valg = (input(""))
    if valg == '1':
        kjemioppg() #Sender brukeren til kjemioppgaven
    elif valg == '2':
        fysikkoppg() #Sender brukeren til fysikkoppgaven
    elif valg == '3':
        biooppgave() #Sender brukeren til biologioppgaven
    elif valg == '4':
        matte() #Sender brukeren til mattematikoppgaven
    elif valg == '5':
        print ("Restarting...")
        time.sleep(3)
        exit()
    else:
        print ("")
startfunksjon() #Starter hele programmet
