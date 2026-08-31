import chromadb

CHROMA_PATH = "chroma_store"
COLLECTION_NAME ="course_documents"

class ChromaStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path= CHROMA_PATH
        )

        self.collection =(
    self.client.get_or_create_collection(
        name = COLLECTION_NAME,
        configuration={
            "hnsw":{
                "space" : "cosine"
            }
        }
    )
)

    def add_documents(
            self,
            documents,
            embeddings
    ):
        ids = []

        texts = []

        metadatas = []

        for index,document in enumerate(documents):

            ids.append(
                f"doc_{index}"
            )

            texts.append(
                document["page_content"]
            )

            metadata =document["metadata"].copy()
            metadata ={
                key: value
                for key,value in metadata.items()
                if value is not None
            }

            metadatas.append(metadata)


        self.collection.add(
            ids= ids,
            documents = texts,
            embeddings = embeddings.tolist(),
            metadatas=metadatas
        )