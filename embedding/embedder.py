from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"


class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(
            MODEL_NAME,
            device = "cpu" 

        )

    def embed_text(self,text):
        """
        Generate an embedding for one piece of text.
        """

        return self.model.encode(text)

    def embed_documents(self,documents):
        """
        Generate embeddings for multiple documents."""

        texts = [
            document["page_content"]
            for document in documents
        ]

        return self.model.encode(
            texts,
            show_progress_bar = True
        )