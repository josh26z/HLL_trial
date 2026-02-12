def extract_structural_features(text: str):
    tokens = text.split()
    ngrams = []

    for i in range(len(tokens) - 2):
        ngrams.append(" ".join(tokens[i:i+3]))

    return ngrams


def extract_role_features(text: str):
    role_keywords = ["system", "developer", "override", "ignore", "policy", "rules"]
    features = []

    for word in role_keywords:
        if word in text:
            features.append(word)

    return features
