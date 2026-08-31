from .embedder import Embedder

embedder = Embedder()

text = "Which courses teach SAP FICO?"

embedding = embedder.embed_text(text)

print("Embedding type :", type(embedding))
print("Embedding shape:", embedding.shape)
print("First 10 values:")
print(embedding[ :10])