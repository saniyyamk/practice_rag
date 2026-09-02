from retrieval.chroma_store import ChromaStore


store = ChromaStore()

print("=" *60)
print("CHROMA COLLECTION")
print("=" *60)

print(
    "collection:",
    store.collection.name
)

print(
    "Document count:",
    store.collection.count()
)