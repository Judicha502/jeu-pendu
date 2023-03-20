from tkinter import *
import random

root = Tk() # CREATION DE LA FENETRE RACINE
width, height = 500, 550  # # HAUTEUR ET LARGEUR DE LA FENETRE CREEE
s_width = ((root.winfo_screenwidth() // 2) - (width // 2))  # (LARGEUR DE L'ECRAN) / 2 - (HAUTEUR DE LA FENETRE CREEE) // 2
s_height = ((root.winfo_screenheight() // 2) - (height // 2))  # (HAUTEUR DE L'ECRAN) // 2 - (HAUTEUR DE LA FENETRE CREEE) // 2
root.geometry(f'{width}x{height}+{s_width}+{s_height}')  # APRES LA HAUTEUR ET LARGEUR DE L'ECRAN, LA HAUTEUR ET LARGEUR DE LA FENETRE CREEE DOIVENT ETRE CENTREES
root.title("Hang-man Game")  # TITRE DE LA FENETRE
root.resizable(0, 0)  # LA FENETRE NE PEUT PAS ETRE REDIMENSIONNEE

# création de la figure du pendu #
canvas = Canvas(root, width=500, height=260)  # CRÉATION D'UN CANVAS SUR LEQUEL ON PEUT DESSINER DES LIGNES ET DES FORMES
canvas.pack(pady=30)  # PACKING D'UN CANVAS À AFFICHER SUR LA FENÊTRE
canvas.create_line(150, 260, 250, 260, width=3)  # LIGNE DE BASE DU SUPPORT
canvas.create_line(200, 260, 200, 40, width=3)  # LIGNE DU SUPPORT
canvas.create_line(200, 90, 250, 40, width=3)  # SUPPORT DU SUPPORT
canvas.create_line(200, 40, 300, 40, width=3)  # LIGNE SUPERIEUR DU SUPPORT
canvas.create_line(300, 40, 300, 70, width=3)  # CORDE DU SUPPORT
canvas.create_oval(280, 70, 320, 100, width=3)  # TETE
c5 = canvas.create_line(300, 100, 300, 180, width=3)  # VENTRE
c4 = canvas.create_line(300, 105, 270, 155, width=3)  # BRAS GAUCHE
c3 = canvas.create_line(300, 105, 330, 155, width=3)  # BRAS DROITE
c2 = canvas.create_line(300, 180, 270, 230, width=3)  # PIED GAUCHE
c1 = canvas.create_line(300, 180, 330, 230, width=3)  # PIED DROITE


# ------------------------------------------ FONCTIONS ------------------------------------------- #
# CHOISIR AU HASARD UN MOT DANS UN FICHIER #
def choose():
    with open("liste.txt", "r") as file:
        words = file.read().split(",")
    pick = random.choice(words)
    return pick


# ------------------------------------------ VARIABLES ------------------------------------------- #


# ------------------------------------ MISE EN PAGE ---------------------------------------------- #
lbl = Label(root, font=("Candara", 25, "bold"))  # CRÉATION D'UN LABEL QUI AFFICHERA LE MOT À DÉCOUVRIR
lbl.pack()  # AJOUT DU LABEL DANS LA FENÊTRE

txt = Entry(root, font=("Candara", 25, "bold"), justify=CENTER, relief=GROOVE, bd=2)  # CETTE ZONE EST UTILISÉE PAR L'UTILISATEUR POUR RÉPONDRE
txt.pack(pady=20)  # AJOUT DE LA ZONE DE TEXTE DANS LA FENÊTRE

btn = Button(root, text="SUBMIT", font=("Candara", 25, "bold"), relief=GROOVE, bg="#E3FFDC") # CLIQUEZ SUR CE BOUTON POUR VÉRIFIER SI LA RÉPONSE EST CORRECTE OU NON
btn.pack(pady=20)  # AJOUT DU BOUTON DANS LA FENÊTRE

root.mainloop()  # LANCEMMENT DE LA BOUCLE INFINIE