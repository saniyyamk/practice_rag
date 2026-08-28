from loader import load_all_courses
from chunker import build_module_chunks

courses=load_all_courses()

total_chunks=0
courses_without_chunks =0
chunks_per_course =[]

for course in courses:

    chunks = build_module_chunks(course)

    chunk_count= len(chunks)

    total_chunks +=chunk_count
    chunks_per_course.append(chunk_count)

    if chunk_count ==0:
        courses_without_chunks +=1

print("=" *70)

print("CHUNK ANALYSIS")
print("=" *70)

print(f"Total courses                    :{len(courses)}")
print(f"Total module chunks              :{total_chunks}")
print(f"Courses without chunks           :{courses_without_chunks}")

print()

print(
    f"Average chunks/course             :"
    f"{total_chunks /len(courses) :.2f}"
)

print(
    f"Maximum chunks/course     : "
    f"{max(chunks_per_course)}"

)

print(
    f"Minimum chunks/course     : "
    f"{min(chunks_per_course)}"
)

largest_chunk = None
largest_size = 0

smallest_chunk = None
smallest_size=float("inf")

total_characters = 0

for course in courses:
    chunks = build_module_chunks(course)

    for chunk in chunks:

        size = len(chunk["page_content"])

        total_characters +=size

        if size > largest_size:
            largest_size=size
            largest_chunk = chunk

        if size < smallest_size:
            smallest_size = size
            smallest_chunk = chunk


print("\n" + "=" * 60)
print("CHUNK SIZE ANALYSIS")
print("=" * 60)

print(f"Total characters : {total_characters}")
print(
    f"Average characters/chunk : "
    f"{total_characters / total_chunks:.2f}"
)

print(f"Largest chunk characters  : {largest_size}")
print(f"Smallest chunk characters : {smallest_size}")

print("\n" + "-" * 60)
print("LARGEST CHUNK")
print("-" * 60)

print("Course:")
print(largest_chunk["metadata"]["course_name"])

print("Module:")
print(largest_chunk["metadata"]["module_index"])

print("\nContent:")
print(largest_chunk["page_content"])