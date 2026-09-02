from embedding.embedder import Embedder
from .chroma_store import ChromaStore

class ChromaRetriever:

    def __init__(self):

        self.store= ChromaStore()
        self.embedder = Embedder()

    def search(
            self,
            query,
            top_k = 5,
            candidate_k =20
    ):

        #1. Embed query......................

        query_embedding = self.embedder.embed_text(
            query
        )

        #2.Build chroma query................

        query_args ={
            "query_embeddings":[
                query_embedding.tolist()
            ],
            "n_results": candidate_k
        }

        #3.Optimal metadata filtering

        if filters:

            conditions=[]

            for key,value in filters.items():

                conditions.append({
                    key:{
                        "$eq":value
                    }
                })

            if len(conditions) == 1:

                query_args["where"] == conditions[0]
            else:

                query_args["where"]={
                    "$end": conditions
                }

    #4.Retrievedocuments from Chroma

    results = self.store.collection.query(
        **query_args
    )

    documents =results["documents"][0]
    metadatas =results["metadatas"][0]
    distances =results["distances"][0]


    #5. Group retieved documents by course

    courses ={}

    for document , metadata, distances