from ingestion.loader import load_all_courses
from ingestion.document_builder import build_document
from ingestion.chunker import build_module_chunks
from .embedder import Embedder


def build_documents():
    """
    Build all course-level and module-level documents."""

    courses = load_all_courses()

    documents =[]

    for course in courses:
        # course level document
        course_document = build_document(course)

        course_document["metadata"]["document-type"] = "course"

        documents.append(course_document)

        #Module-level documents

        module_documents = build_module_chunks(course)

        documents.extend(module_documents)

    return documents

if __name__ == "__main__":

    documents = build_documents()

    print("=" *60)
    print("DOCUMENT CORPUS")
    print("="*60)

    print(f"Total documents: {len(documents)}")

    print("\nFirst document:")
    print(documents[0]["page_content"])

    print("\nMetadata:")
    print(documents[0]["metadata"])


    print("\nGenerating embeddings......")

    embedder = Embedder()

    embeddings = embedder.embed_documents(documents)

    print("\n" + "=" *60)
    print("EMBEDDING RESULT")
    print("=", 60)

    print("Documents:", len(documents))
    print("Embedding shape:", embeddings.shape)