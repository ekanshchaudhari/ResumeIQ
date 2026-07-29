import re


def extract_email(text):
    """
    Extracts the first email address found in the text.
    """

    pattern = r"[A-Za-z0-9._-]+@[A-Za-z]+\.[A-Za-z]+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None