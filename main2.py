import pyterrier as pt
import os

os.environ["JAVA_HOME"] = "/lib/jvm/java-11-openjdk-amd64/"
pt.init()

dataset = pt.datasets.get_dataset("vaswani")

# indexer = pt.TRECCollectionIndexer("./vaswani-index")
# indexref = indexer.index(dataset.get_corpus())
# index = pt.IndexFactory.of(indexref, verbose= True)

index = pt.IndexFactory.of("/home/nitin/Desktop/BTP/vaswani-index/data.properties")
# print(index.getCollectionStatistics().toString())

tf_idf = pt.BatchRetrieve(index, wmodel="TF_IDF")
bm25 = pt.BatchRetrieve(index, wmodel="BM25")
pl2 = pt.BatchRetrieve(index, wmodel="PL2")

# result = pt.Experiment([tf_idf, bm25, pl2], dataset.get_topics(), dataset.get_qrels(), eval_metrics=["map"])

# print(result)
# print(tf_idf)
print(dataset.get_qrels().head(10))