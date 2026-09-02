
from .build_chroma import build_documents

from embedding.embedder import Embedder
from vector_store.vector_store import save_vector_store


def main():
    print("=" *60)
    print("BUILDING VECTOR SCORE")
    print("=" *60)

    documents = build_documents()

    print(f"Documents: {len(documents)}")

    print("\nLoading embedding model.....")

    embedder= Embedder()

    print("\nGenerating embedding....")

    embeddings= embedder.embed_documents(documents)

    print("\nEmbedding shape:")

    print*(embeddings.shape)

    print("\n Saving Vectore store....")

    save_vector_store(
        embeddings,
        documents
    )

    print("\nDone")



if __name__ =="__main__":
    main()






