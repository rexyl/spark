"""SimpleApp.py"""
from pyspark import SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

sc = SparkContext("local", "Simple App")

documents = sc.textFile('wikiset/ACID').map(lambda line: line.split(" "))
hf = HashingTF()
tf = hf.transform(documents)
tf.cache()
idf = IDF().fit(tf)
tfidf = idf.transform(tf)

# logFile = "hello"  # Should be some file on your system
# sc = SparkContext("local", "Simple App")
# logData = sc.textFile(logFile).cache()

# numAs = logData.filter(lambda s: 'a' in s).count()
# numBs = logData.filter(lambda s: 'b' in s).count()

f = open('result','w')
f.write(tfidf)
#f.write("Lines with a: %i, lines with b: %i" % (numAs, numBs))
f.close()
