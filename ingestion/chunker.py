def build_module_chunks(course):


    outline = course["course_outline"]

    if not outline:
        return []

    if isinstance(outline,dict):
        outline=[outline]

    chunks= []

    for index, item in enumerate(outline, start=1):
        if not isinstance(item,dict):
            continue

        module = 