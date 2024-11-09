"""
Ce module lit l'entrée de l'utilisateur et l'affiche dans la console.
"""

def lire_invite():
    """Lit et affiche ce que l'utilisateur saisit jusqu'à ce que 'exit' soit saisi."""
    while True:
        texte = input("Écris quelque chose (ou tape 'exit' pour quitter) : ")
        if texte.lower() == "exit":
            print("Programme terminé.")
            break
        print(f"Tu as écrit : {texte}")

lire_invite()
