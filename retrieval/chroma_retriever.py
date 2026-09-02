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

        