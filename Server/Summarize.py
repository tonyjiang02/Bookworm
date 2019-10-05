# detect language
from langdetect import detect
lang = detect(cleaned_email) # lang = 'en' for an English email

#Sentence Tokenization with nltk
from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(email, language = lang)

#Skip-Gram Word2Vec Skip-Thought Encoder converts sentences to vectors
#weighted sum: weights are inversely related to word frequency

#encoder network: generates sentence vector
#decoder network: guesses previous and next sentences (neighboring sentences)

# The 'skipthoughts' module can be found at the root of the GitHub  repository linked in documentation
import skipthoughts

# You would need to download pre-trained models first
model = skipthoughts.load_model()

encoder = skipthoughts.Encoder(model)
encoded =  encoder.encode(sentences)
