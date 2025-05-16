def detect_fraudulent_cv(text):
    fake_keywords = ["chatgpt", "openai", "prompt", "fictive", "fake experience"]
    return any(word in text.lower() for word in fake_keywords)
