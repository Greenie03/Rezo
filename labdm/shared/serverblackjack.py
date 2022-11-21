import random
from os import system, name
import time
import asyncio

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


async def handle_request(reader, writer):
    data = await reader.read(668) # gets a message ...
    writer.write(data.decode()[::-1].encode()) # ... reverse it before sending it back
    writer.close()


async def reversi_server():
    # start a socket server
    server = await asyncio.start_server(handle_request, '0.0.0.0', 668)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever() # handle requests for ever


if __name__ == '__main__':
    asyncio.run(reversi_server())



























# Classe carte
class Cartes:
    def __init__(self, suite, valeur, carte_valeur):
         
        # Suite des carte tel que coeur pique ...
        self.suite = suite
 
        # Représentation des cartes Roi, As ...
        self.valeur = valeur
 
        # Valeur des cartes
        self.carte_valeur = carte_valeur
 

# Clear le terminal
def clear():
    if name == 'nt':
        _ = system('cls')
 
# Affiche la carte passée en parametre, si celle-ci n'est pas dissimulée
def print_cartes(cartes, dissimulé):
         
    s = ""
    for carte in cartes:
        s = s + "\t ________________"
    if dissimulé:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for carte in cartes:
        if carte.valeur == '10':
            s = s + "\t|  {}            |".format(carte.valeur)
        else:
            s = s + "\t|  {}             |".format(carte.valeur)  
    if dissimulé:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for carte in cartes:
        s = s + "\t|       {}        |".format(carte.suite)
    if dissimulé:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|                |"
    print(s)
 
    s = ""
    for carte in cartes:
        s = s + "\t|                |"
    if dissimulé:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for carte in cartes:
        if carte.valeur == '10':
            s = s + "\t|            {}  |".format(carte.valeur)
        else:
            s = s + "\t|            {}   |".format(carte.valeur)
    if dissimulé:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for carte in cartes:
        s = s + "\t|________________|"
    if dissimulé:
        s += "\t|________________|"
    print(s)        
 
    print()
 
 
# Game blackjack
def blackjack_game(deck):
 
    # Cartes du joueur et dealeur
    joueur_cartes = []
    dealer_cards = []
 
    # Score du joueur et dealer
    joueur_score = 0
    dealer_score = 0
 
    clear()
 
    while len(joueur_cartes) < 2:
 
        joueur_carte = random.choice(deck)
        joueur_cartes.append(joueur_carte)
        deck.remove(joueur_carte)
 
        joueur_score += joueur_carte.carte_valeur
 
        if len(joueur_cartes) == 2:
            if joueur_cartes[0].carte_valeur == 11 and joueur_cartes[1].carte_valeur == 11:
                joueur_cartes[0].carte_valeur = 1
                joueur_score -= 10

        print("CARTES JOUEUR: ")
        print_cartes(joueur_cartes, False)
        print("SCORE JOUEUR = ", joueur_score)
 
        input("Tapez ok pour continuer :")
 
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Update score
        dealer_score += dealer_card.carte_valeur
 
        print("CARTES CROUPIER: ")
        if len(dealer_cards) == 1:
            print_cartes(dealer_cards, False)
            print("CROUPIER SCORE = ", dealer_score)
        else:
            print_cartes(dealer_cards[:-1], True)    
            print("CROUPIER SCORE = ", dealer_score - dealer_cards[-1].carte_valeur)
 
 
       
        if len(dealer_cards) == 2:
            if dealer_cards[0].carte_valeur == 11 and dealer_cards[1].carte_valeur == 11:
                dealer_cards[1].carte_valeur = 1
                dealer_score -= 10
 
        input("Tapez ok pour continuer :")
 
    # Joueur a le blackjack   
    if joueur_score == 21:
        print("LE JOUEUR A LE BLACKJACK!!!!")
        print("LE JOUEUR A GAGNE!!!!")
        quit()
 
    clear()
 
    # Print dealer et joueur cartes
    print("CARTES CROUPIER: ")
    print_cartes(dealer_cards[:-1], True)
    print("CROUPIER SCORE = ", dealer_score - dealer_cards[-1].carte_valeur)
 
    print() 
 
    print("CARTES JOUEUR: ")
    print_cartes(joueur_cartes, False)
    print("SCORE JOUEUR = ", joueur_score)
 
   
    while joueur_score < 21:
        choice = input("Entrez P pour Prendre ou R pour Rester : ")
 
        
        if len(choice) != 1 or (choice.upper() != 'P' and choice.upper() != 'R'):
            clear()
            print("Mauvais choix!! Essaye encore")
 
        # Le joueur prend
        if choice.upper() == 'P':
 
            
            joueur_carte = random.choice(deck)
            joueur_cartes.append(joueur_carte)
            deck.remove(joueur_carte)
 
            # Update joueur score
            joueur_score += joueur_carte.carte_valeur
 
           
            c = 0
            while joueur_score > 21 and c < len(joueur_cartes):
                if joueur_cartes[c].carte_valeur == 11:
                    joueur_cartes[c].carte_valeur = 1
                    joueur_score -= 10
                    c += 1
                else:
                    c += 1 
 
            clear()     
 
            # Print joueur et dealer cartes
            print("CARTES CROUPIER: ")
            print_cartes(dealer_cards[:-1], True)
            print("CROUPIER SCORE = ", dealer_score - dealer_cards[-1].carte_valeur)
 
            print()
 
            print("CARTES JOUEUR: ")
            print_cartes(joueur_cartes, False)
            print("SCORE JOUEUR = ", joueur_score)
             
        # Si joueur reste
        if choice.upper() == 'R':
            break
 
 
    clear() 
 
    # Print joueur et delaer cartes
    print("CARTES JOUEUR: ")
    print_cartes(joueur_cartes, False)
    print("SCORE JOUEUR = ", joueur_score)
 
    print()
    print("LE CROUPIER REVELE LES CARTES....")
 
    print("CARTES CROUPIER: ")
    print_cartes(dealer_cards, False)
    print("CROUPIER SCORE = ", dealer_score)
 
    # Check si le joueur a le blackjack
    if joueur_score == 21:
        print("LE JOUEUR A LE BLACKJACK")
        quit()
 
    # Check si le joueur depasse
    if joueur_score > 21:
        print("LE JOUEUR A DEPASSER!!! PERDU!!!")
        quit()
 
    input("Tapez ok pour continuer :") 
 
    
    while dealer_score < 17:
        clear() 
 
        print("LE CROUPIER DECIDE DE PRENDRE.....")
 
       
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        
        dealer_score += dealer_card.carte_valeur
 
        # Update score
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].carte_valeur == 11:
                dealer_cards[c].carte_valeur = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1
 
        # print joueur et dealer cartes
        print("CARTES JOUEUR: ")
        print_cartes(joueur_cartes, False)
        print("SCORE JOUEUR = ", joueur_score)
 
        print()
 
        print("CARTES CROUPIER: ")
        print_cartes(dealer_cards, False)
        print("CROUPIER SCORE = ", dealer_score)      
 
        input("Tapez ok pour continuer :")
 
    # Dealer depasse
    if dealer_score > 21:        
        print("LE CROUPIER A DEPASSER!!! VOUS AVEZ GAGNE!!!") 
        quit()  
 
    # Le dealer a le blackjack
    if dealer_score == 21:
        print("LE CROUPIER A LE BLACKJACK!!! LE JOUEUR A PERDUE")
        quit()
 
    # Match nul
    if dealer_score == joueur_score:
        print("MATCH NUL!!!!")
 
    # Joueur Wins
    elif joueur_score > dealer_score:
        print("LE JOUEUR A GAGNE!!!")                 
 
    # Dealer Wins
    else:
        print("LE CROUPIER A GAGNE!!!")                 
 
if __name__ == '__main__':
 
    
    suites = ["♠", "♥", "♣", "♦"]
 
    # Valeur des suites 
    suites_valeur = {"♠":"\u2664", "♥":"\u2661", "♣": "\u2667", "♦": "\u2662"}
 
    # Types de cartes
    cartes = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # Valeur des cartes
    cartes_valeurs = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    # Le deck des cartes
    deck = []
 
    # Boucle pour tout type de suites
    for suite in suites:
 
        # Boucle pour tous les types de cartes dans une suite
        for carte in cartes:
 
            # Ajouter la carte au deck
            deck.append(Cartes(suites_valeur[suite], carte, cartes_valeurs[carte]))
     
    blackjack_game(deck)  
