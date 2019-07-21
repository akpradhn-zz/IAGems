
# coding: utf-8

# ### Objective : Cluster Documents and find top 5 common term from each cluster.

# Topic Covered
# * Cluster Algorithms
#     - K-Means 
# * Different types of similarity measures
#     - Euclidean distance:
#     - Manhattan distance:
#     - Cosine similarity:    

# In[226]:


# Final Libraries
from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import re #Cleaning Documents
import pandas as pd #Creating Dataframes
import numpy as np
import random # Freeding Randonness
from sklearn.feature_extraction.text import TfidfVectorizer # For Vectorization
from sklearn.feature_extraction.text import CountVectorizer # Count Vectors
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import laplacian_kernel
from sklearn.metrics.pairwise import linear_kernel
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score # Finding Optimum number of clusters Number 
import matplotlib.pyplot as plt # Visualization


# In[228]:


# Options Settings
pd.set_option('display.max_columns', None) # To Print Every column of a data frame


# ### 1. Collecting Data
# 
# For this mini project, we are collecting abstracts from first 10 search result for the query 'Asthma' in PubMed database using the API provided on the website. The complete code is available below..

# In[231]:


def fetch_abstract(key_word,abst_n):
    
    '''
    Objective:
    ----------
    Returns a list of abstracts of reqired number for a searct quiry from pubmed data base.
    
    Argumnets.
    ----------
    key_word (string): search query text. For e.g. neurodegenerative diseases 
    abst_n  (numeric): Number of Documents required For e.g. 100 
    
    Return:
    -------
    Return a List of abstracts
    
    '''
    '''
    First API to collect PMIDs for abstracts for a search text query
    '''

    payload1 = {'term':key_word, 'retmax' : '15'}
    response1 = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',params=payload1)
    soup = BeautifulSoup(response1.content, 'html.parser')
    
    print('PMIDs fetched !')
    
    s=[]
    
    ''' 
    Second API to collect abstracts for a required PMID
    '''

    print('Fetching Abstracts...')
    
    for link in soup.find_all('id'):
        
        payload2 = {'db':'pubmed','id':link.string,'rettype':'abstract'}
        tempabs = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi',params = payload2)
        result = BeautifulSoup(tempabs.content, 'html.parser')
    
        try:
            abs= result.find('abstracttext')
            clean=abs.string
            
        except AttributeError:
            pass

        # Store Abstract into a list
        s.append(clean)

        # keeping tract of number of abstract collectd
        if len(s) % 10 == 0:
            progress = len(s)/abst_n * 100
            print(" {}% complete.".format(round(progress, 1)))
                    
    abs_list=s[0:abst_n]
    print(abst_n, ' Abstracts fetched')
    
    return(abs_list)


# #### Collecting 10 abstracts for the 'Asthma'

# In[232]:


key_word = 'Asthma'
abst_n = 10
corpus = fetch_abstract(key_word,abst_n)


# In[230]:


print('Number of Documents in the raw data corpus: ',format(len(corpus)))
print('First 2 Documents :','\n',corpus[0])


# ### 2. Cleaning Data
# 
# Types of Cleaning
# * Removing Numerics Data
# * Removing Non-ASCII Characters

# In[213]:


def cleanText(raw_text):
    '''
    Objective:
    ----------
    Remove Numeric and Punctuations from a String.
    
    Argument
    --------
    A string.
    
    Reurn
    -------
    A string without numeric/Special character
    
    '''
    #stopword_set = set(stopwords.words("english"))
    return "".join([i for i in re.sub(r'[^\w\s]|\d|','',raw_text)])

clean_corpus = [cleanText(x) for x in corpus]


# In[214]:


print("Raw Text","\n",corpus[0])
print("Clean Text","\n",clean_corpus[0])


# ### 3. Next Step : Document to Vector 
#     Vector can be a Countervector or a TFIDF Vector

# In[215]:


countVec = CountVectorizer(stop_words='english')

# Vectors or Term Document Matrix 
tdm_Y = countVec.fit_transform(clean_corpus)

# Get Words from Unique 
unique_words2 = countVec.get_feature_names()

print("The Documents has", len(unique_words2)," words.")

#print(unique_words)
df_Y = pd.DataFrame(tdm_Y.toarray(), columns=unique_words2)
#print(tdm_Y.todense())

display(df_Y)


# ### 3.1 Lets understand how TFIDF is calculated.
# 
# The Clean corpus containing 408 words wherein the word 'adult' appears 3 times.
# The term frequency (i.e., tf) for cat is then (3 / 408) = 0.007.
# 
# Now, we have 10 documents and the word 'adult' appears only in one of these (i.e. 9th Documnets).
# Then, the inverse document frequency (i.e., idf) is calculated as log(10 / 1) = 2.303
# 
# Thus, the Tf-idf weight for 'adult' is the product of these quantities: 0.03 * 2.303 = 0.016.
# 
# In the Next step these weights are then normalised wrt other words in a documents and the final TFIDF matrix can be calculated.
# 

# In[233]:


tfidVec = TfidfVectorizer(stop_words='english')

# Vectors or Term Document Matrix 
tdm_X = tfidVec.fit_transform(clean_corpus)

# Get Words from Unique 
unique_words = tfidVec.get_feature_names()

print("The Documents has", len(unique_words)," words.")

#print(unique_words)
#print(tdm_X.todense())

df_X = pd.DataFrame(tdm_X.toarray(), columns=unique_words)
#type(df_X)
display(df_X)


# In[234]:


cos_sim = cosine_similarity(tdm_X[0:1],tdm_X)
euc_sim = euclidean_distances(tdm_X[0:1],tdm_X)
mah_sim = manhattan_distances(tdm_X[0:1],tdm_X)


# #### Cosine Similarity

# In[235]:


cos_sim


# Document 1 is similar to Document 6 and 10

# #### Euclidean Similarity
# 

# In[236]:


euc_sim


# This array shows how far the documents vectors are from Document 1. The closer the more similarity.
# 
# Its clearly upto the coide of user to determine the criteria to asses the similarity between tow documents.

# ### 4. K-Mean Clustering

# Determining Best number of Clusters 
# 

# In[223]:


Clusters = []
Silh_Coefficient = []

for n_cluster in range(2, 10):
    kmeans = KMeans(n_clusters=n_cluster, init='k-means++', max_iter=100, n_init=3).fit(tdm_X)
    label = kmeans.labels_
    sil_coeff = silhouette_score(tdm_X, label, metric='euclidean')
    Clusters.append(n_cluster)
    Silh_Coefficient.append(sil_coeff)
    #print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))

plt.plot(Clusters, Silh_Coefficient)
plt.title('Finding Best Number of Cluster')
plt.xlabel('Number of Cluster')
plt.ylabel('Silhouette_Score')

plt.show()


# In[224]:


true_k = 6
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=3)
model.fit(tdm_X)

clusters = model.labels_.tolist()
print(clusters)


# In[225]:


print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = tfidVec.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    print("----------------")
    for ind in order_centroids[i, :5]:
        print(" ",terms[ind])
    print("\n")


# ## References: Some Cool Examples
# 
# 
# * [Document Clustering with Python](http://brandonrose.org/clustering) (Most Suggested)
# 
# * [K-Means clustering on the handwritten digits data](http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html)
# 
# * [The Data Science Lab:Clustering With K-Means in Python](https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/)
# 
# * [kmeans text clustering](https://pythonprogramminglanguage.com/kmeans-text-clustering/)
# 
# * http://ethen8181.github.io/machine-learning/clustering_old/tf_idf/tf_idf.html
# 
# * [Different types of similarity measures](http://dataaspirant.com/2015/04/11/five-most-popular-similarity-measures-implementation-in-python/)
# 
# * [Finding Number Of Cluster : Wikipedia](https://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3BGYqlkK3tQ3%2Bb3VWBSvgP8Q%3D%3D)
# * [K-means clustering: how it works - Youtube](https://www.youtube.com/watch?v=_aWzGGNrcic&lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3BGYqlkK3tQ3%2Bb3VWBSvgP8Q%3D%3D)
# * [KMeans++ Explained](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
# 
