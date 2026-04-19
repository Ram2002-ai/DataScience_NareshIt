import pandas as pd
import numpy as np

df=pd.read_csv(r"E:\data\data_set\Restaurant_Reviews.tsv",delimiter='\t',quoting=3)

import re
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus=[]

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
    
from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()

y=df.iloc[:,1].values


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier(max_depth=200)
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score


accuracy=accuracy_score(y_test, y_pred)

bias=classifier.score(X_train,y_train)

variance=classifier.score(X_test,y_test)


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf=TfidfVectorizer(
    max_features=1000,
    ngram_range=(1,2)
    )

X=tfidf.fit_transform(corpus).toarray()


from sklearn.naive_bayes import GaussianNB

gb=GaussianNB()

gb.fit(X_train,y_train)

gb=gb.predict(X_test)

gb_acc=accuracy_score(y_test, y_pred)



# word2vec
from gensim.models import Word2Vec

model=Word2Vec(
    sentences=corpus,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4
    )


vectors=model.wv.vectors

print(corpus)
print(len(set(corpus)))
