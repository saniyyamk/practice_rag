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
            candidate_k =20,
            filters = None
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

        for document , metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):
            course_name = metadata["course_name"]
            #chroma returns cosine distance
            #converts distance to similarity.

            score= 1 - distance

            if course_name not in courses:
                courses[course_name] = {
                    "course_name" : course_name,
                    "department" : metadata["department"],
                    "course_category":metadata["course_category"],
                    "evidence":[]
                }

            courses[course_name]["evidence"].append({
                "score" : score,
                "document_type" : metadata["document_type"],
                "document" : document,
                "metadata" : metadata
            })

        # 6. Calculate best score for each course

        ranked_courses = []

        for course in courses.values():
            
            course["best_score"] = max(
                evidence["score"]
                for evidence in course["evidence"]
            )

            ranked_courses.append(course)

        # 7.Rank courses

        ranked_courses.sort(
            key = lambda course : course [
                "best_score"
            ],
            reverse = True
        )

        # 8 .Return top courses

        return ranked_courses[:top_k]