#!/usr/bin/env python3

import os
import re
import json
import nltk
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

def get_posting(file):
    co0p_job = dict()

    with open(file, 'r') as f:
        text = f.read()
        try:
            info, desc = text.split('Job Description:')
        except:
            info1, info2, desc = text.split('Job Description:')
            info = info1 + info2
        info = info.split(':')
        
        co0p_job['org'] = text.split('Organization Name')[-1].split('\n')[0]

        new_info = []
        for i in range(1, len(info)):
            info[i] = info[i].split('\n')
            try:
                new_info.append(info[i][-1] + info[i+1].split('\n')[0])
            except:
                pass

        if desc[0] == ' ':
            desc = desc[1:]

        co0p_job.update({'info': new_info, 'description': desc})

        return co0p_job

JOBS = dict()
for _,_,files in os.walk('./postings'):
    for file in files:
        if file.endswith('.txt'):
            JOBS[file.split('.')[0].split('_')[-1]] = get_posting('postings'+'/'+file)

documents = []
for job_id, job in JOBS.items():
    text_content = ' '.join([job['org']] + job['info'] + [job['description']])
    documents.append(text_content)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

def find_relevant_jobs(query):
    query_vec = vectorizer.transform([query])
    cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()
    related_docs_indices = cosine_similarities.argsort()[:-5:-1]
    relevant_jobs = [(index, cosine_similarities[index]) for index in related_docs_indices]
    return relevant_jobs

def chatbot_response(query):
    relevant_jobs = find_relevant_jobs(query)
    # print(relevant_jobs)
    response = "Jobs based on TF-IDF:\n"
    for index, score in relevant_jobs:
        response += f"{index}\n"
    return response

def recommend_jobs(user_query, jobs_data):
    query_tokens = re.findall(r'\b\w+\b', user_query.lower())
    
    scored_jobs = []
    for job_id, job in jobs_data.items():
        score = 0
        description = job.get('description', '').lower()
        for token in query_tokens:
            score += description.count(token)
        scored_jobs.append((job_id, score))
    
    scored_jobs.sort(key=lambda x: x[1], reverse=True)
    
    return [job_id for job_id, score in scored_jobs if score > 0][:5]

while True:
    query = input("Enter your query: ")
    print("Jobs based on exact match of query words:", recommend_jobs(query, JOBS))
    print(chatbot_response(query))