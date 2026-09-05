from sentence_transformers import CrossEncoder

class Reranker:

    def __init__(self):

        print("Loading reranker....")

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L6-v2",
            device = "cpu"
        )

    def rerank(
        self,
        query,
        documents,
        top_k =5
    ):

        if not documents:
            return []

        pairs = [
            [query,document]
            for document in documents
        ]

        scores = self.model.predict(
            pairs
        )

        ranked = sorted(
            zip(documents, scores),
            key = lambda item: float(item[1]),
            reverse = True
        )

        return ranked[:top_k]

