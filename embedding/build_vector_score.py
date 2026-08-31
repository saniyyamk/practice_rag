from ingestion.loader import load_all_courses
from ingestion.document_builder import build_document
from ingestion.chunker import build_module_chunks

from embedding.embedder import Embedder

from retrieval.chroma_store import ChromaStore

def build_documents():
    courses = load_all_courses()

    documents = []

    for course in courses:
        #course document

        course_document = build_document(course)

        course_document["metadata"]["document_type"]  = "course"

        documents.append(course_document)

        #Module documents

        module_documents = build_module_chunks(course)

        documents.extend(module_documents)

    return documents


def main():

    print("=" *60)
    print("BUILDING CHROMA VECTOR STORE")
    print("=" *60)

    documents = build_documents()

    print(
        f"Documents: {len(documents)}"
    )

    print("\nLoading embedding model....")

    embedder = Embedder()

    print("\nGenerating embedding...")

    embeddings = embedder.embed_documents(documents)

    print(
        f"Embedding shape : {embeddings.shape}"
    )

    print("\nCreating chroma score...")

    store=ChromaStore()

    print("\nAdding documents")

    store.add_documents(
        documents,
        embeddings
    )

    print("\nDone")


if __name__ =="__main__":
    main()




    


