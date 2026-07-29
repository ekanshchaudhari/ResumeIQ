import pdfplumber


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from an uploaded PDF file.

    Parameters:
        uploaded_file: The PDF file uploaded through Streamlit.

    Returns:
        A string containing all the text found in the PDF.
    """

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text