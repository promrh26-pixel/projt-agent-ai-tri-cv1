def compute_score(features):

    score = 0

    score += features["experience"] * 2
    score += len(features["skills"]) * 5
    score += len(features["languages"]) * 2

    return score
