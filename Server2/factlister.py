import spacy
import textacy.extract

def eventLister(text):
    # Load the large English NLP model
    nlp = spacy.load('en_core_web_lg')

    # Parse the document with spaCy
    doc = nlp(text)

    # Extract semi-structured statements
    statements = textacy.extract.semistructured_statements(doc, "text")

    # Return the results
    for statement in statements:
        subject, verb, fact = statement
        return(f" - {fact}")
