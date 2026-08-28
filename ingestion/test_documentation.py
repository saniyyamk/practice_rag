from loader import load_all_courses
from document_builder import build_document

courses=load_all_courses()
print(len(courses))
for course in courses:

    outline = course["course_outline"]
    print
    if (
        isinstance(outline, list)
        and outline
        and isinstance(outline[0], dict)
        and "title" in outline[0]
    ):

        document = build_document(course)

        print("=" * 70)
        print("RICH OUTLINE EXAMPLE")
        print("=" * 70)

        print(document["page_content"])

        print("\nMETADATA:")
        print(document["metadata"])

        break