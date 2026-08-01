import pdfplumber
import fitz


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.
    """

    text = ""

    uploaded_file.seek(0)

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_links_from_pdf(uploaded_file):
    """
    Extracts all hyperlinks from an uploaded PDF.
    """

    links = []

    uploaded_file.seek(0)

    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in doc:
        page_links = page.get_links()

        for link in page_links:
            if "uri" in link:
                links.append(link["uri"])

    doc.close()

    return links