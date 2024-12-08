import matplotlib.pyplot as plt
from wordcloud import WordCloud

def afficher_scores(scores, avis_originaux):
    """Affiche un histogramme des scores de sentiment."""
    plt.figure(figsize=(10, 6))
    couleurs = ['green' if score > 0 else 'red' if score < 0 else 'gray' for score in scores]
    plt.bar(range(len(scores)), scores, color=couleurs)
    plt.xticks(range(len(avis_originaux)), [f"Avis {i+1}" for i in range(len(avis_originaux))], rotation=45)
    plt.ylabel("Score de Sentiment")
    plt.title("Analyse de Sentiment des Avis")
    plt.show()

def generer_nuage_mots(avis_nettoyes, titre):
    """Génère et affiche un nuage de mots pour les avis donnés."""
    texte = ' '.join(avis_nettoyes)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texte)
    plt.figure(figsize=(10, 6))
    plt.title(titre)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
