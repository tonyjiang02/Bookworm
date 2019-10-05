#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for E-mail Summarization
*****************************************************************************
Input Parameters:
    emails: A list of strings containing the emails
Returns:
    summary: A list of strings containing the summaries.
*****************************************************************************
"""


# ***************************************************************************
import numpy as np
from talon.signature.bruteforce import extract_signature
from langdetect import detect
from nltk.tokenize import sent_tokenize
import skipthoughts
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
# ***************************************************************************
emails = ["Well, Prince, so Genoa and Lucca are now just family estates of the Buonapartes. \n But I warn you, if you don’t tell me that this means war, if you still try to defend the infamies and horrors perpetrated by that Antichrist—I really believe he is Antichrist—I will have nothing more to do with you and you are no longer my friend, no longer my ‘faithful slave,’ as you call yourself! But how do you do? I see I have frightened you—sit down and tell me all the news."]

def split_sentences(emails):
    """
    Splits the emails into individual sentences
    """
    n_emails = len(emails)
    for i in range(n_emails):
        email = emails[i]
        sentences = sent_tokenize(email)
        for j in reversed(range(len(sentences))):
            sent = sentences[j]
            sentences[j] = sent.strip()
            if sent == '':
                sentences.pop(j)
        emails[i] = sentences


def skipthought_encode(emails):
    """
    Obtains sentence embeddings for each sentence in the emails
    """
    enc_emails = [None]*len(emails)
    cum_sum_sentences = [0]
    sent_count = 0
    for email in emails:
        sent_count += len(email)
        cum_sum_sentences.append(sent_count)

    all_sentences = [sent for email in emails for sent in email]
    print('Loading pre-trained models...')
    model = skipthoughts.load_model()
    encoder = skipthoughts.Encoder(model)
    print('Encoding sentences...')
    enc_sentences = encoder.encode(all_sentences, verbose=False)

    for i in range(len(emails)):
        begin = cum_sum_sentences[i]
        end = cum_sum_sentences[i+1]
        enc_emails[i] = enc_sentences[begin:end]
    return enc_emails


def summarize(emails):
    """
    Performs summarization of emails
    """
    n_emails = len(emails)
    summary = [None]*n_emails
    print('Splitting into sentences...')
    split_sentences(emails)
    print('Starting to encode...')
    enc_emails = skipthought_encode(emails)
    print('Encoding Finished')
    for i in range(n_emails):
        enc_email = enc_emails[i]
        n_clusters = int(np.ceil(len(enc_email)**0.5))
        kmeans = KMeans(n_clusters=n_clusters, random_state=0)
        kmeans = kmeans.fit(enc_email)
        avg = []
        closest = []
        for j in range(n_clusters):
            idx = np.where(kmeans.labels_ == j)[0]
            avg.append(np.mean(idx))
        closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_,\
                                                   enc_email)
        ordering = sorted(range(n_clusters), key=lambda k: avg[k])
        summary[i] = ' '.join([emails[i][closest[idx]] for idx in ordering])
    print('Clustering Finished')
    return summary

split_sentences(emails)
skipthought_encode(emails)
summarize(emails)
print (summary)
