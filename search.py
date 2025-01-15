from rank_bm25 import BM25Plus
import numpy as np
import preprocess as pre
from dataset import get_data


df = get_data()



def inference(query, model, k=1):
    def softmax(scores):
        exp_scores = np.exp(scores - np.max(scores))  # Stabilité numérique
        return exp_scores / np.sum(exp_scores)

    def k_argmax(scores, k=k):
        indices_tries = np.argsort(scores)[::-1]  # Tri décroissant
        return indices_tries[:k]

    tokenized_query = pre.tokenize(query)
    doc_scores = softmax(model.get_scores(tokenized_query))
    doc_indexes = k_argmax(doc_scores)
    doc_scores = np.sort(doc_scores)[::-1][:k]

    # Dictionnaire pour stocker le résultat final
    results = {}

    for i in range(k):
        index = doc_indexes[i].item()
        score = doc_scores[i].item()
        description = df.loc[index, 'Description']  # Utiliser le DataFrame pour obtenir la description
        image_path = df.loc[index, 'Chemin_d_acces']  # Utiliser le DataFrame pour obtenir le chemin de l'image

        results[index] = (score, description, image_path)

    return results

def get_model(tokenized_corpus=pre.get_tokenized_corpus()):
    bm25 = BM25Plus(tokenized_corpus)
    return bm25

"""model = get_model()
query = input("Entrez votre requête: ")
best_docs = inference(query, model)


print("\n\n\nRésultats de la recherche:")
for index, (score, description) in best_docs.items():
    print(f"Score: {score}")
    print(f"Description: {description}")
    pre.plot_image(index)
    print("\n")
    """