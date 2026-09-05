from .chroma_retriever import ChromaRetriever

def main():

    print("Loading retriever.....")

    retriever = ChromaRetriever()

    query = "Which courses teach AI?"

    filters = None

    print("=" *70)
    print("QUERY")
    print("=" *70)

    print(query)

    print("\n")
    print("=" *70)
    print("FILTERS")
    print("=" *70)

    print(filters)

    results = retriever.search(
        query = query,
        top_k = 5,
        candidate_k =20,
        filters = filters
    )

    print("\n")
    print("=" *70)
    print("TOP COURSES")
    print("=" *70)

    for rank,result in enumerate(
        results,
        start =1
    ):
        print("\n")
        print("-" * 70)

        print(f"Rank: {rank}")

        print(
            f"Course"
            f"{result['course_name']}"
        )

        print(
            f"Department: "
            f"{result['department']}"
        )

        print(
            f"Category: "
            f"{result['course_category']}"
        )

        print(
            f"Reranker score: "
            f"{result['best_score']:.4f}"
        )

        print("\nEvidence:")

        for evidence in result["evidence"]:
            print(
                f" "
                f"{evidence['document_type']}"
                f" ->"
                f"{evidence['score']:.4f}"
            )

if __name__ == "__main__":
    main()