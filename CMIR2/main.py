import pyterrier as pt
import os
import sys
import stopwords

os.environ["JAVA_HOME"] = "/lib/jvm/java-11-openjdk-amd64/"

experiments = ["baseline"]

# val1 = int(sys.argv[1])/100
# val2 = int(sys.argv[2])/100
# val1 = 4.12


mode = 'combined-tfidf'
for x in experiments:
    # stopwords.create_stopwords(val1, 0, mode)
    pt.init()
    # create the index
    files = [f'dataset/{x}/{x}_corpus.trec']
    # shutil.rmtree('index/')
    indexer = pt.TRECCollectionIndexer(f"./index/{x}_index/ind", stemmer = None)
    indexref = indexer.index(files)

    # index = pt.IndexFactory.of(f'/home/nitin/Desktop/BTP/CMIR2/index/{x}_index/data.properties')
    index = pt.IndexFactory.of(indexref)
    # print(index.getCollectionStatistics().toString())

    tf_idf = pt.BatchRetrieve(index, wmodel="TF_IDF")
    bm25 = pt.BatchRetrieve(index, wmodel="BM25")
    pl2 = pt.BatchRetrieve(index, wmodel="PL2")
    InL2 = pt.BatchRetrieve(index, wmodel="InL2")
    Hiemstra_LM = pt.BatchRetrieve(index, wmodel="Hiemstra_LM")

    # result = pt.Experiment([bm25], pt.io.read_topics(f'dataset/{x}/{x}_query.trec'), pt.io.read_qrels(f'QRels_new_50.txt'), eval_metrics=["map"], verbose = True, perquery = True)
    result = pt.Experiment([tf_idf, bm25, pl2, InL2, Hiemstra_LM], pt.io.read_topics(f'dataset/{x}/{x}_query.trec'), pt.io.read_qrels(f'QRels_new_50.txt'), eval_metrics=["map", "recip_rank", "ndcg", "P_5", "P_10"], verbose = True)
    print(result)
    
    
    # result.to_csv(f'results/only_stopwords/Combined/tfidf/best_result/{val1}_per_query.csv')
    result.to_csv('baseline.csv')
    