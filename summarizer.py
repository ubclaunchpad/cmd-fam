#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 22:59:34 2019

@author: sanid
"""
#importing important libraries
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS) #loading all the stopwords into a list


nlp = spacy.load("en")   
#sample input text
document1 ="""Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. 
Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. 
Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. 
Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. 
Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""

#creating an instance of spacy
docx = nlp(document1)

mytokens = [token.text for token in docx]

# word.text is tokenization(makes the word into its token) in spacy
word_frequencies = {} #hash map storing the occurences of each token in the input text
for word in docx:
    if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


maximum_frequency = max(word_frequencies.values())  #max frequency is the most amount of times a word was repeated


for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency) #creating scores/weights for each token


sentence_list = [ sentence for sentence in docx.sents ] #evaluating score of each sentence using the scores of which words they contain

sentence_scores = {}  
for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]


headline = max(sentence_scores, key= sentence_scores.get) #sentence with highest score will be headline


