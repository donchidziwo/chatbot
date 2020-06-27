#!/usr/bin/env python
# coding: utf-8

# # Load data preprocessing libraries

# In[ ]:


import pandas as pd
import numpy as np


# # Load vectorizer and similarity measure

# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ## Read the data and drop rows with no data

# In[ ]:


df = pd.read_csv("aws_faq.csv")
df.dropna(inplace=True)


# ## Train the vectorizer

# In[ ]:


vectorizer = TfidfVectorizer()
vectorizer.fit(np.concatenate((df.Question, df.Answer)))


# ## Vectorize questions

# In[ ]:


Question_vectors = vectorizer.transform(df.Question)


# 
# ## Chat with the user

# In[ ]:


def bot_response(input_question):
    # Read user input
    # input_question = input() => Parameter in bot_response is taking care of that now

    # Locate the closest question
    input_question_vector = vectorizer.transform([input_question])

    # Compute similarities
    similarities = cosine_similarity(input_question_vector, Question_vectors)

    # Find the closest question
    closest = np.argmax(similarities, axis=1)

    # Print the correct answer
    # print("BOT: " + df.Answer.iloc[closest].values[0]) => We now return instead of print
    answer = df.Answer.iloc[closest].values[0]
    return answer