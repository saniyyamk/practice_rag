from retrieval.re_ranker import Reranker


def main():

    reranker = Reranker()

    query = "Which courses teach FICO?"

    documents = [
        """
        Course: Diploma in Corporate Finance & Control - SAP

        Objective:
        The program equips learners with practical skills
        in SAP Finance and Controlling (FICO) modules.

        Curriculum:
        Module 3: SAP Finance and Controlling
        - SAP Finance & Controlling - Basics
        - SAP Power User - FICO
        """,

        """
        Course: Diploma in International Finance Management with SAP FICO

        Objective:
        The course combines international accounting,
        finance and SAP FICO for enterprise resource planning.

        Curriculum:
        Module 4: SAP Finance Module
        - SAP FICO - Power User
        """,

        """
        Course: Diploma in Finance Management with SAP FICO & Tally

        Curriculum:
        Module 3: ERP Accounting
        - SAP FICO - Power User
        """,

        """
        Course: Diploma in International Finance Management with SAP S/4 HANA

        Curriculum:
        Module 4: SAP Finance Module
        - SAP FICO - Power User (SAP S/4 HANA)
        """,

        """
        Course: Diploma in SAP Material Management

        Objective:
        This course equips students with skills required
        to work on SAP MM modules.

        Curriculum:
        Module 2: SAP Material Management
        - SAP Material Management - Basics
        - SAP Power User - MM
        """
    ]

    results = reranker.rerank(
        query = query,
        documents = documents,
        top_k =5
    )

    print("="*70)
    print("RERANKER TEST")
    print("="*70)

    for rank, (document, score) in enumerate(
        results,
        start = 1
    ):

        print("\n" + "-" * 70)

        print(f"Rank :{rank}")

        print(f"Score: {float(score):.4f}")

        print(document)

if __name__ == "__main__":
    main()