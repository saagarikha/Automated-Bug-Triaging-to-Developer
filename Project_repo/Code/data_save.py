from sklearn.externals import joblib
from pandas import DataFrame
import numpy
val=0
def build_data_frame(path, classification):
  global val
  data_frame = DataFrame({'text': [], 'class': []})
  data_frame = data_frame.append(
  	DataFrame({'text': [path], 'class': [classification]}, index=[val]))
  val=val+1	
  return data_frame

def confusion_matrix(conf_arr,name):
	norm_conf = []
	for i in conf_arr:
		a = 0
		tmp_arr = []
		a = sum(i,0)
		for j in i:
		        tmp_arr.append(float(j)/float(a))
		norm_conf.append(tmp_arr)

	plt.clf()
	fig = plt.figure()
	ax = fig.add_subplot(111)
	res = ax.imshow(array(norm_conf), cmap=cm.jet, interpolation='nearest')
	for i, cas in enumerate(conf_arr):
	    for j, c in enumerate(cas):
		if c>0:
		    plt.text(j-.2, i+.2, c, fontsize=14)
	cb = fig.colorbar(res)
	savefig(name, format="png")


f = open('output_devnew.txt')
var=[]
li=[]
pair1=()
for line in f :
	pair=line.decode('UTF-8').rstrip().rsplit(',',1)
	if len(pair)== 2 :	
		if True == (pair[1] not in li): 	
			 li.append(pair[1])			  
		pair1=pair[0],li.index(pair[1])  
		var.append(pair1)

data = DataFrame({'text': [], 'class': []})
for path, classification in var:
  data = data.append(build_data_frame(path, classification))

data = data.reindex(numpy.random.permutation(data.index))
joblib.dump(data, 'data_new.pkl', compress=9)
