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
def extract_phone(text):
    """
    Extracts an Indian phone number from the text.
    """

    pattern = r"(\+91[\s-]?)?[0-9]{10}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None
def extract_linkedin(text):
    """
    Extracts a LinkedIn profile URL from the text.
    """

    pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None
def extract_github(text):
    """
    Extracts a GitHub profile URL from the text.
    """

    pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+/?"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None