from ingestion.loader import load_all_courses
from ingestion.document_builder import build_document
from ingestion.chunker import build_module_chunks

from embedding.embedder import Embedder

from .similarity import cosine_similarity

class Retriever:

    def __init__(self):

        self.embedder = Embedder()

        self.documents = self._build_documents()

        self.embeddings = self.embedder.embed_documents(
            self.documents
        )

    def _build_documents(self):
        courses = load_all_courses()

        documents =[]

        for course in courses:

            #course-level document
            course_document = build_document(course)

            course_document["metadata"]["document_type"] ="course"

            documents.append(course_document)

            #Module-level documents
            module_documents=build_module_chunks(course) 

            documents.extend(module_documents)

        return documents


    def search(self,query, top_k=5):

        query_embedding = self.embedder.embed_text(query)

        scores = cosine_similarity(
            query_embedding,
            self.embeddings
        )

        top_indices = scores.argsort()[-top_k:][::-1]

        results= []

        for index in top_indices:

            results.append({
                "score": float(scores[index]),
                "document":self.documents[index]
            })

        return results

    def search_courses(self, query, top_k=5):
        query_embedding = self.embedder.embed_text(query)

        scores=cosine_similarity(
            query_embedding,
            self.embeddings
        )

    #sort all documents by similarity

        ranked_indices=scores.argsort()[::-1]

        courses ={

        }

        for index in ranked_indices:

            document =self.documents[index]
            metadata= document["metadata"]

            course_name = metadata["course_name"]

            score= float(scores[index])

            if course_name not in courses:

                courses[course_name] = {
                    "course_name" :course_name,
                    "best_score" :score,
                    "evidence" :[]
                }

                courses[course_name]["evidence"].append({
                    "score" : score,
                    "document_type": metadata["document_type"],
                    "document":document
                })

        #Sort courses accprding to their stromgest evidence
            ranked_courses =sorted(
                courses.values(),
                key = lambda x: x["best_score"],
                reverse = True
            )

            return ranked_courses[:top_k]