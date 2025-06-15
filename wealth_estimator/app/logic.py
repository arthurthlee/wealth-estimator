import numpy as np
import json
from sklearn.metrics.pairwise import cosine_similarity

def find_top_matches(user_embedding, top_n_similar: int = 3):
    with open("app/data/data.json", "r") as f:
        WEALTHY_PROFILES = json.load(f)

    names = []
    embeddings = []
    net_worths = []

    for name, values in WEALTHY_PROFILES.items():
        names.append(name)
        embeddings.append(np.array(values["embedding"]))
        net_worths.append(values["net_worth"])

    similarities = cosine_similarity([user_embedding], embeddings)[0]
    top_indices = similarities.argsort()[::-1][:top_n_similar]

    matches = []
    estimated_wealth = 0.0
    total_sim = sum([similarities[i] for i in top_indices])

    for i in top_indices:
        matches.append({
            "name": names[i],
            "similarity": round(float(similarities[i]), 4)
        })
        estimated_wealth += similarities[i] * net_worths[i]

    if total_sim > 0:
        estimated_wealth /= total_sim

    return matches, round(estimated_wealth)
