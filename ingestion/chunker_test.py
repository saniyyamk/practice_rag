from loader import load_all_courses

from chunker import build_module_chunks

courses = load_all_courses()

for course in courses:

    outline = course["course_outline"]

    if(
        isinstance(outline, list)
        and outline
        and isinstance(outline[0], dict)
        and "title" in outline[0]
    ):
        chunks = build_module_chunks(course)

        print("=" *70)

        print(course)
        print("=" *70)

        print(course["course_name"])

        print("\nNUMBER OF MODEL CHUNKS:")
        print(len(chunks))

        for chunk in chunks:
            print("\n" + "-" *70)

            print(chunk["page_content"])

            print("\n METADATA")

            print(chunk["metadata"])
        break
