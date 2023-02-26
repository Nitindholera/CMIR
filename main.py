import pyterrier as pt
import os

os.environ["JAVA_HOME"] = "/lib/jvm/java-11-openjdk-amd64/"
pt.init()

# print(pt.datasets.list_datasets())

dataset = pt.datasets.get_dataset('irds:cord19/trec-covid')
indexer = pt.index.IterDictIndexer('./cord19-index')
indexref = indexer.index(dataset.get_corpus_iter(), fields=('title', 'abstract'))
index = pt.IndexFactory.of(indexref)

print(dataset)

DPH_br = pt.BatchRetrieve(index, wmodel="DPH") % 100
BM25_br = pt.BatchRetrieve(index, wmodel="BM25") % 100
# this runs an experiment to obtain results on the TREC COVID queries and qrels
pt.Experiment(
    [DPH_br, BM25_br],
    dataset.get_topics('title'),
    dataset.get_qrels(),
    eval_metrics=["P.5", "P.10", "ndcg_cut.10", "map"])