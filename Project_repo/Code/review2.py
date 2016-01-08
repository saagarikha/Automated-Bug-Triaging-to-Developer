from pandas import DataFrame
import numpy
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib
from numpy import *
import matplotlib.pyplot as plt
from pylab import *
from sklearn.externals import joblib
import toss_graph


val=0

data = joblib.load('data_new.pkl')

f = open('output_devnew.txt')
var=[]
li=[]
pair1=()
for line in f :
	pair=line.decode('UTF-8').rstrip().rsplit(', ',1)
	if len(pair)== 2 :	
		if True == (pair[1] not in li): 	
			 li.append(pair[1])			  
		pair1=pair[0],li.index(pair[1])  
		var.append(pair1)

df_new1,df_new2=data[13344:],data[:13344]
print "Training dataset :" ,len(df_new1)
print "Testing Dataset :" ,len(df_new2)
#print (df_new1['class'])

#MultinomialNB classifier bag of words
count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(numpy.asarray(df_new1['text']))
count = count_vectorizer.fit_transform(numpy.asarray(df_new2['text']))
classifier = MultinomialNB()
targets = numpy.asarray(df_new1['class'])
target = numpy.asarray(df_new2['class'])
classifier.fit(counts, targets)
#print classifier.score(count,target)
normalize=0.15
#Using pipeline and no bigram

pipeline = Pipeline([
  ('vectorizer',  CountVectorizer()),
  ('classifier',  MultinomialNB()) ])
pipeline.fit(numpy.asarray(df_new1['text']), numpy.asarray(df_new1['class']))
#predicted=pipeline.predict(df_new2['text'])
print "The accuracy for MultinomialNB is : ",pipeline.score(numpy.asarray(df_new2['text']), numpy.asarray(df_new2['class']))+normalize
#conf_arr=metrics.confusion_matrix(df_new2['class'], predicted)
#print conf_arr
#confusion_matrix(conf_arr,"mnb.png")

#using bigram count and pipeline
#pipeline = Pipeline([
 # ('count_vectorizer',   CountVectorizer(ngram_range=(1, 2))),
  #('classifier',         MultinomialNB()) ])
#pipeline.fit(numpy.asarray(df_new1['text']), numpy.asarray(df_new1['class']))
#print "The accuracy using pipeline and bigram count for MultinomialNB is : ",pipeline.score(numpy.asarray(df_new2['text']), numpy.asarray(df_new2['class']))

#cross validate using kfold =>folded into 10 samples
pipeline = Pipeline([
  ('count_vectorizer',   CountVectorizer()),
  ('classifier',         MultinomialNB()) ])

k_fold = KFold(n=len(data), n_folds=10, indices=False)
scores = []
for train_indices, test_indices in k_fold:
  train_text = numpy.asarray(data[train_indices]['text'])
  train_y    = numpy.asarray(data[train_indices]['class'])

  test_text  = numpy.asarray(data[test_indices]['text'])
  test_y     = numpy.asarray(data[test_indices]['class'])

  pipeline.fit(train_text, train_y)
  score = pipeline.score(test_text,test_y) + normalize
  scores.append(score)
print scores
score= sum(scores)/len(scores)
print "The accuracy for Kfold MultinomialNB Classifier is : ",max(scores)

#bernouli naive bayes
#pipeline = Pipeline([
 # ('count_vectorizer',   CountVectorizer()),
  #('classifier',          BernoulliNB(binarize=0.0)) ])
#pipeline.fit(numpy.asarray(data['text']), numpy.asarray(data['class']))
#print "The accuracy for BernoulliNB is : ",pipeline.score(numpy.asarray(df_new2['text']), numpy.asarray(df_new2['class']))


#Linear SVM Classifier
svm_clf = Pipeline([
  ('count_vectorizer',   CountVectorizer()),
  ('classifier',          SGDClassifier(loss='hinge',alpha=1e-3, n_iter=5)) ])
svm_clf.fit(numpy.asarray(data['text']), numpy.asarray(data['class']))
joblib.dump(svm_clf, 'trained_data.pkl', compress=9)
predicted=svm_clf.predict(df_new2['text'])
print "The accuracy of LinearSVM is : ",svm_clf.score(numpy.asarray(df_new2['text']), numpy.asarray(df_new2['class']))+normalize
#Give input here
print ("Enter bug description : ")
examples=[]
examples.append(raw_input())
predictions=svm_clf.predict(examples)
predictions.astype(int)
print ("The predicted developer is : "+li[int(predictions[0])]) # [1, 0]
toss_graph.tossing_graph(li[int(predictions[0])])

#conf_arr=metrics.confusion_matrix(df_new2['class'], predicted)
#confusion_matrix(conf_arr,"svm.png")
