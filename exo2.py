# Liste pour stocker les étudiants
etudiants = []

# Implémentez une fonction ajouter_etudiant
def ajouter_etudiant(nom, age, notes):
    etudiant = (nom, age, notes)
    etudiants.append(etudiant)

# Implémentez une fonction afficher_etudiants
def afficher_etudiants():
    for etudiant in etudiants:
        nom, age, notes = etudiant
        print(f"Nom: {nom}, Âge: {age}, Notes: {notes}")

# mplémentez une fonction calculer_moyenne
def calculer_moyenne(notes):
    if not notes:  # Vérifie si la liste de notes est vide
        return 0
    return sum(notes) / len(notes)

# Fonction pour trouver l'étudiant avec la meilleure moyenne
def meilleure_moyenne():
    if not etudiants:  # Vérifie si la liste d'étudiants est vide
        return None
    meilleur_etudiant = max(etudiants, key=lambda etudiant: calculer_moyenne(etudiant[2]))
    return meilleur_etudiant

# Fonction pour trier et afficher les étudiants par leur moyenne
def trier_etudiants_par_moyenne():
    etudiants_tries = sorted(etudiants, key=lambda etudiant: calculer_moyenne(etudiant[2]), reverse=True)
    for etudiant in etudiants_tries:
        nom, age, notes = etudiant
        moyenne = calculer_moyenne(notes)
        print(f"Nom: {nom}, Âge: {age}, Moyenne: {moyenne:.2f}")

# Exemple d'utilisation
ajouter_etudiant("ALEXIS", 20, [15, 18, 12])
ajouter_etudiant("NAZAIRE", 22, [14, 17, 19])
ajouter_etudiant("YANN", 21, [13, 16, 14])

print("Informations des étudiants :")
afficher_etudiants()

print("\nMoyenne des notes de chaque étudiant :")
for etudiant in etudiants:
    nom, age, notes = etudiant
    moyenne = calculer_moyenne(notes)
    print(f"Nom: {nom}, Moyenne: {moyenne:.2f}")

print("\nÉtudiant avec la meilleure moyenne :")
meilleur_etudiant = meilleure_moyenne()
if meilleur_etudiant:
    nom, age, notes = meilleur_etudiant
    print(f"Nom: {nom}, Âge: {age}, Moyenne: {calculer_moyenne(notes):.2f}")

print("\nInformations des étudiants triés par leur moyenne :")
trier_etudiants_par_moyenne()
