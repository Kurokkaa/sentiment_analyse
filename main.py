from preprocessing import charger_et_nettoyer_donnees
from sentiment_analysis import analyser_ensemble
from visualization import afficher_scores, generer_nuage_mots

def main():
    # Charger et nettoyer les données
    chemin_fichier = './data/reviews.txt'
    avis_originaux = [line.strip() for line in open(chemin_fichier, 'r', encoding='utf-8')]
    avis_nettoyes = charger_et_nettoyer_donnees(chemin_fichier)

    # Analyser le sentiment des avis
    scores = analyser_ensemble(avis_nettoyes)

    # Afficher les résultats
    for avis, score in zip(avis_originaux, scores):
        sentiment = "Positif" if score > 0 else "Négatif" if score < 0 else "Neutre"
        print(f"{avis} -> Score : {score:.2f} ({sentiment})")

    # Visualisations
    afficher_scores(scores, avis_originaux)
    generer_nuage_mots([avis_nettoyes[i] for i, score in enumerate(scores) if score > 0], "Nuage de mots - Avis Positifs")
    generer_nuage_mots([avis_nettoyes[i] for i, score in enumerate(scores) if score < 0], "Nuage de mots - Avis Négatifs")

if __name__ == "__main__":
    main()
