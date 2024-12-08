from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

def analyser_sentiment(texte):
    """Analyse le sentiment d'un texte et retourne le score."""
    blob = TextBlob(texte, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return blob.sentiment[0]  # Retourne le score de polarité (positif, négatif, neutre)

def analyser_ensemble(avis_nettoyes):
    """Analyse le sentiment d'une liste d'avis nettoyés."""
    scores = [analyser_sentiment(avis) for avis in avis_nettoyes]
    return scores
