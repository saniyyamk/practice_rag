from .retrieval import Retriever

retriever = Retriever()

query ="hey which courses teach AI?"

results = retriever.search_courses(
    query,
    top_k=5
)

print("=" * 70)
print("QUERY")
print("=" * 70)

print(query)


print("\n" + "=" * 70)
print("TOP RESULTS")
print("=" * 70)

for rank,result in enumerate(results, start=1):
    print("\n" + "-" * 70)

    print(f"Rank: {rank}")
    print(f"Course: {result['course_name']}")
    print(f"Best score: {result['best_score']:.4f}")

    print("\nEvidence:")

    for evidence in result["evidence"][:3]:

        print(
            f"  {evidence['document_type']} "
            f"→ {evidence['score']:.4f}"
        )