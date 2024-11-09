def lire_invite():
    while True:
        texte = input("Écris quelque chose (ou tape 'exit' pour quitter) : ")
        if texte.lower() == "exit":
            print("Programme terminé.")
            break
        else:
            print(f"Tu as écrit : {texte}")

lire_invite()