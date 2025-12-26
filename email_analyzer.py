import re

def analyze_email(content):
    score = 0
    reasons = []

    if re.search(r'http[s]?://', content):
        score += 1
        reasons.append("Contains links")

    if any(word in content.lower() for word in ["urgent", "verify", "password", "bank"]):
        score += 2
        reasons.append("Suspicious language")

    if score >= 2:
        return "PHISHING ⚠️", reasons
    return "SAFE ✅", reasons
