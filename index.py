# Executer avant :
# pip install -r requirements.txt
# python nltk_data.py
# python -m spacy download fr_core_news_lg
# python -m spacy download fr_core_news_sm

# import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *


# import field extractor
from information.nom import * 
from information.education import * 
from information.telephone import * 
from information.email import * 
from information.competence import * 
import lecteurfichiers.pdf2text as pdf2text



def process(initial_filepath, root):
    from tkinter import filedialog as fd

    # Obtenir le chemin du fichier de l'utilisateur via une boîte de dialogue (uniquement les fichiers PDF)
    chemin_fichier = fd.askopenfilename(initialdir=initial_filepath, title='Sélectionner le fichier', filetypes=(('fichiers PDF', '*.pdf'),))
    
    texte = pdf2text.get_Text(chemin_fichier)

    nom              = extraire_nom(texte)
    numero_telephone = extraire_numero_telephone(texte)
    email            = extraire_email(texte)
    education        = extraire_education(texte)
    competences      = extraire_competences(texte)

    fenetre_resultat = tk.Tk()
    fenetre_resultat.title("Informations extraites")
    fenetre_resultat.geometry("800x300")

    tk.Label(fenetre_resultat, text="Informations extraites", font=("Arial", 20)).grid(row=0, column=1, pady=10)

    tk.Label(fenetre_resultat, text="Nom \t: ").grid(row=1, column=0, sticky="w", padx=10)
    tk.Label(fenetre_resultat, text=f"{nom}").grid(row=1, column=1, sticky="w", padx=10)

    tk.Label(fenetre_resultat, text="Éducation\t: ").grid(row=2, column=0, sticky="w", padx=10)
    tk.Label(fenetre_resultat, text=f"{education}").grid(row=2, column=1, sticky="w", padx=10)

    tk.Label(fenetre_resultat, text="Téléphone\t: ").grid(row=3, column=0, sticky="w", padx=10)
    tk.Label(fenetre_resultat, text=f"{numero_telephone}").grid(row=3, column=1, sticky="w", padx=10)

    tk.Label(fenetre_resultat, text="Email\t: ").grid(row=4, column=0, sticky="w", padx=10)
    tk.Label(fenetre_resultat, text=f"{email}").grid(row=4, column=1, sticky="w", padx=10)

    tk.Label(fenetre_resultat, text="Compétences\t: ", anchor="w", justify=LEFT).grid(row=5, column=0, sticky="w", padx=10)
    tk.Label(fenetre_resultat, text="\n".join(competences), anchor="w", justify=LEFT, wraplength=200).grid(row=5, column=1, sticky="w", padx=10)


 
if __name__ == '__main__':
    from tkinter import filedialog as fd
    
    # Créer une fenêtre de 600x300 et centrer cela sur l'écran.
    largeur = 600
    hauteur = 300

    root = tk.Tk()
    root.title("Analyseur de CV")
    
    largeur_ecran = root.winfo_screenwidth()
    hauteur_ecran = root.winfo_screenheight()
    x = (largeur_ecran/2) - (largeur/2)
    y = (hauteur_ecran/2) - (hauteur/2)
    
    root.geometry('%dx%d+%d+%d' % (largeur, hauteur, x, y))

    # Créer un bouton de boîte de dialogue de fichier.
    bouton = ttk.Button(root, text='Parcourir le fichier')
    bouton.config(command=lambda chemin_fichier='.': process(chemin_fichier, root))
    bouton.pack(fill=X)

    root.mainloop()
