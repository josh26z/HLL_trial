def extract_structural_features(text: str):
    tokens = text.split()
    ngrams = []

    for i in range(len(tokens) - 2):
        ngrams.append(" ".join(tokens[i:i+3]))

    if not ngrams:
        ngrams = tokens  # fallback for short input

    return ngrams


def extract_role_features(text: str):
    role_keywords = [
        "system",
        "developer",
        "override",
        "ignore",
        "policy",
        "rules",
        "admin",
        "internal"
    ]

    return [word for word in role_keywords if word in text]