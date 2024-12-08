import re
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')


def nettoyer_texte(texte):
    """Nettoie le texte en supprimant la ponctuation et les mots vides."""
    texte = texte.lower()
    texte = re.sub(r'[^\w\s]', '', texte)
    mots_vides = set(stopwords.words('french'))
    mots = re.findall(r'\w+', texte)  # Utilisation simple de regex pour la tokenisation
    mots = [mot for mot in mots if mot not in mots_vides]
    return ' '.join(mots)


def charger_et_nettoyer_donnees(fichier):
    """Charge les avis depuis un fichier et les nettoie."""
    with open(fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
    return [nettoyer_texte(avis.strip()) for avis in lignes]


def main():
    # Charger et nettoyer les données
    chemin_fichier = './data/reviews.txt'
    avis_originaux = [line.strip() for line in open(chemin_fichier, 'r', encoding='utf-8')]
    avis_nettoyes = charger_et_nettoyer_donnees(chemin_fichier)

    # Fonctionnalités fictives pour l'analyse des sentiments et la visualisation
    def analyser_ensemble(avis):
        return [0] * len(avis)  # Remplacement par [0] pour les scores

    def afficher_scores(scores, avis):
        pass

    def generer_nuage_mots(avis, title):
        pass

    # Analyser le sentiment des avis
    scores = analyser_ensemble(avis_nettoyes)

    # Afficher les résultats
    for avis, score in zip(avis_originaux, scores):
        sentiment = "Positif" if score > 0 else "Négatif" if score < 0 else "Neutre"
        print(f"{avis} -> Score : {score:.2f} ({sentiment})")

    # Visualisations
    afficher_scores(scores, avis_originaux)
    generer_nuage_mots([avis_nettoyes[i] for i, score in enumerate(scores) if score > 0],
                       "Nuage de mots - Avis Positifs")
    generer_nuage_mots([avis_nettoyes[i] for i, score in enumerate(scores) if score < 0],
                       "Nuage de mots - Avis Négatifs")


if __name__ == "__main__":
    main()
