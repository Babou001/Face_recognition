from rank_bm25 import BM25Plus
import numpy as np
import preprocess as pre


def inference(query, model, k=1):
    def softmax(scores):
        """
        Applique la fonction softmax à un tableau de scores.

        :param scores: Liste ou tableau de scores.
        :return: Tableau de probabilités résultant de l'application de softmax.
        """
        # Calcul de l'exponentielle des scores en soustrayant le max pour la stabilité numérique
        exp_scores = np.exp(scores - np.max(scores))

        # Normalisation pour obtenir des probabilités
        return exp_scores / np.sum(exp_scores)

    def k_argmax(scores, k=k):
        """
        Renvoie les indices des k scores les plus élevés dans un tableau.

        :param scores: Liste ou tableau contenant les scores.
        :param k: Le nombre d'indices à renvoyer (correspondant aux scores les plus élevés).
        :return: Liste des indices des k scores les plus élevés, triés par ordre décroissant.
        """
        # Utilisation de np.argsort pour obtenir les indices triés
        indices_tries = np.argsort(scores)[::-1]  # Tri décroissant
        return indices_tries[:k]

    tokenized_query = pre.tokenize(query)
    doc_scores = softmax(model.get_scores(tokenized_query))
    doc_indexes = k_argmax(doc_scores)
    doc_scores = np.sort(doc_scores)[::-1][:k]
    scores_dict = {}
    for i in range(k):
        index = doc_indexes[i].item()
        scores_dict[index] = doc_scores[i].item() , pre.get_description(index)
    return scores_dict
    
    

def get_model(tokenized_corpus=pre.get_tokenized_corpus()):
    bm25 = BM25Plus(tokenized_corpus)
    return bm25

model = get_model()
query = input("Entrez votre requête: ")
best_docs = inference(query, model)


print("\n\n\nRésultats de la recherche:")
for index, (score, description) in best_docs.items():
    print(f"Score: {score}")
    print(f"Description: {description}")
    pre.plot_image(index)
    print("\n")
