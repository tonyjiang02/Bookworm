# detect language
from langdetect import detect
lang = detect(cleaned_email) # lang = 'en' for an English email

#Sentence Tokenization with nltk
from nltk.tokenize import sent_tokenize
email = "Hi my name is Tony and I am looking for a job."
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

# Clustering: number of clusters = desired sentences in summary
import numpy as np
from sklearn.cluster import KMeans

n_clusters = np.ceil(len(encoded)**0.5)
kmeans = KMeans(n_clusters=n_clusters)
kmeans = kmeans.fit(encoded)

#Summarization: one sentence, whose vector is closest to center, is chosen from each cluster
from sklearn.metrics import pairwise_distances_argmin_min

avg = []
for j in range(n_clusters):
    idx = np.where(kmeans.labels_ == j)[0]
    avg.append(np.mean(idx))
closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, encoded)
ordering = sorted(range(n_clusters), key=lambda k: avg[k])
summary = ' '.join([email[closest[idx]] for idx in ordering])
