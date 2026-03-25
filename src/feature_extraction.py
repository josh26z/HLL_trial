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
    r"developer\s*mode",
    r"admin\s*(mode|access|control)",
    r"reveal.*policy",
    r"ignore.*policy",
    r"ignore.*instruction",
    r"bypass.*safety",
    r"bypass.*filter",
    r"override.*system",
    r"system\s*prompt",
    r"jailbreak",
    r"act\s*as\s*system",
]

    return [word for word in role_keywords if word in text]