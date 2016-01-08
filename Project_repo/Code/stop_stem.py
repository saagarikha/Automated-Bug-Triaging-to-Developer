
from nltk.stem.porter import *
from nltk.corpus import stopwords

stop=stopwords.words('english')
stemmer=PorterStemmer()
f = open('output_dev')
fp=open('output_devnew.txt','w')
var=[]
for line in f :
	for word in line.decode('utf-8').split() :
		if word not in stop :
			fp.write(stemmer.stem(word).encode('utf-8'))
			fp.write(' ')
	fp.write('\n')
fp.close()
