import numpy as np
import json
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

def find_top_matches(user_embedding: np.ndarray, top_n_similar: int = 3):
    # If no user embedding was found, return an empty array for matches, and None for estimated wealth
    if len(user_embedding) == 0:
        return [], None

    with open(Path("wealth_estimator/data/data.json"), "r") as f:
        WEALTHY_PROFILES = json.load(f)

    names = []
    embeddings = []
    net_worths = []

    # Loop through the dictionary containing the names of the wealthy individuals, and the values (containing their net worth and face embeddings)
    for name, values in WEALTHY_PROFILES.items():
        names.append(name)
        embeddings.append(np.array(values["embedding"]))
        net_worths.append(values["net_worth"])

    # Find the cosine similarity between the user_embedding and all the existing precomputed embeddings
    # We're only passing in one user embedding at a time, so we can just take the first similarity
    similarities = cosine_similarity([user_embedding], embeddings)[0]
    print(cosine_similarity([user_embedding], embeddings))
    # Get the N most similar pictures
    top_indices = similarities.argsort()[::-1][:top_n_similar]

    matches = []
    estimated_wealth = 0.0
    total_sim = sum([similarities[i] for i in top_indices])

    # For each of the top N matches, keep track of their name, and their corresponding similarity score
    for i in top_indices:
        matches.append({
            "name": names[i],
            "similarity": round(float(similarities[i]), 4)
        })
        # Add up the estimated wealth to be the similarity score * net worth of each returned match
        # Ex. Jeff Bezos has similarity score of 0.8 and net worth of $10 = $8
        # Bill gates has similarity score of 0.5 and net worth of $8 = $4
        # Summed estimated wealth = $8 + $4
        estimated_wealth += similarities[i] * net_worths[i]

    if total_sim > 0:
        # Now divide the summed esimated wealth with the summed similarity scores of all matches
        # This gives a weighted average of the net worths of all the matches
        estimated_wealth /= total_sim

    return matches, round(estimated_wealth)
