"""
Programme de gestion de bibliothèque.
Permet de gérer une collection de livres : ajouter, rechercher, marquer comme emprunté ou retourné, et lister les livres.
"""

from datetime import datetime

class Livre:
    """Classe représentant un livre dans la bibliothèque."""
    
    def __init__(self, titre, auteur, categorie, annee):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.annee = annee
        self.emprunte = False
        self.date_emprunt = None

    def emprunter(self):
        """Marque le livre comme emprunté."""
        if not self.emprunte:
            self.emprunte = True
            self.date_emprunt = datetime.now()
            print(f"Le livre '{self.titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.titre}' est déjà emprunté.")

    def retourner(self):
        """Marque le livre comme retourné."""
        if self.emprunte:
            self.emprunte = False
            duree_emprunt = (datetime.now() - self.date_emprunt).days
            self.date_emprunt = None
            print(f"Le livre '{self.titre}' a été retourné. "
                  f"Durée d'emprunt : {duree_emprunt} jours.")
        else:
            print(f"Le livre '{self.titre}' n'est pas actuellement emprunté.")

    def __str__(self):
        status = "emprunté" if self.emprunte else "disponible"
        return (f"{self.titre} par {self.auteur} ({self.annee}) - "
                f"{self.categorie} - {status}")


class Bibliotheque:
    """Classe représentant une bibliothèque."""

    def __init__(self):
        self.collection = []

    def ajouter_livre(self, titre, auteur, categorie, annee):
        """Ajoute un nouveau livre à la collection."""
        livre = Livre(titre, auteur, categorie, annee)
        self.collection.append(livre)
        print(f"Le livre '{titre}' a été ajouté à la bibliothèque.")

    def rechercher_par_titre(self, titre):
        """Recherche un livre par titre."""
        resultats = [livre for livre in self.collection if titre.lower() in livre.titre.lower()]
        if resultats:
            print("Livres trouvés :")
            for livre in resultats:
                print(livre)
        else:
            print(f"Aucun livre trouvé avec le titre '{titre}'.")

    def lister_par_categorie(self, categorie):
        """Affiche les livres d'une certaine catégorie."""
        resultats = [livre for livre in self.collection
                     if livre.categorie.lower() == categorie.lower()]
        if resultats:
            print(f"Livres dans la catégorie '{categorie}' :")
            for livre in resultats:
                print(livre)
        else:
            print(f"Aucun livre trouvé dans la catégorie '{categorie}'.")

    def afficher_collection(self):
        """Affiche tous les livres de la collection."""
        if self.collection:
            print("Collection de la bibliothèque :")
            for livre in self.collection:
                print(livre)
        else:
            print("La bibliothèque est vide.")

    def emprunter_livre(self, titre):
        """Emprunte un livre par son titre."""
        for livre in self.collection:
            if livre.titre.lower() == titre.lower():
                livre.emprunter()
                return
        print(f"Aucun livre trouvé avec le titre '{titre}'.")

    def retourner_livre(self, titre):
        """Retourne un livre emprunté."""
        for livre in self.collection:
            if livre.titre.lower() == titre.lower():
                livre.retourner()
                return
        print(f"Aucun livre trouvé avec le titre '{titre}'.")


# Exemple d'utilisation du programme de gestion de bibliothèque
bibliotheque = Bibliotheque()

# Ajout de quelques livres
bibliotheque.ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry", "Roman", 1943)
bibliotheque.ajouter_livre("1984", "George Orwell", "Science-fiction", 1949)
bibliotheque.ajouter_livre("Python pour les nuls", "Marcia Hall", "Programmation", 2020)

# Affichage de la collection
bibliotheque.afficher_collection()

# Emprunter un livre
bibliotheque.emprunter_livre("1984")

# Rechercher un livre
bibliotheque.rechercher_par_titre("Python")

# Lister par catégorie
bibliotheque.lister_par_categorie("Roman")

# Retourner un livre
bibliotheque.retourner_livre("1984")

# Affichage final de la collection
bibliotheque.afficher_collection()
