def format_outline(course_outline):


    if not course_outline:
        return "Curriculum information is not available."

    lines=[]
    if isinstance(course_outline,dict):
        course_outline=[course_outline]


    for item in course_outline:

        if not isinstance(item,dict):
            continue


        if isinstance(item.get("module"),str):

            lines.append(
                f"- {item['module']}"
            )

        else:

            module_number =item.get("module")
            title=item.get("title")
            topics=item.get("topics",[])

            if module_number is not None and title:
                lines.append(
                    f"Module {module_number} :{title}"
                )
            elif title:
                lines.append(title)

            for topic in topics:
                lines.append(
                    f" - {topic}"
                )

    return "\n".join(lines)



def build_page_content(course):

    duration = course["duration"]

    duration_parts =[]

    if duration["months"] is not None:
        duration_parts.append(
            f"{duration['months']} months"
        )

    if duration["hours"] is not None:
        duration_parts.append(
            f"{duration['hours']} hours"
        )

    duration_text =", ".join(duration_parts)

    if not duration_text:
        duration_text =duration["raw"]

    outline_text = format_outline(
        course["course_outline"]
    )

    page_content =f"""
Course Name:{course['course_name']}

Department :{course['department']}

Category: {course['course_category']}

Duration:{duration_text}

Objective: {course['objective']}

Curriculum:{outline_text}
""".strip()

    return page_content

def build_metadata(course):
    duration = course["duration"]
    return{
        "course_name" : course["course_name"],
        "department" : course["department"],
        "course_category" :course["course_category"],
        "duration_months" : duration["months"],
        "duration_hours": duration["hours"],
        "source_file" : course["source"]["file"],
        "source_path" : course["source"]["path"]
    }

def build_document(course):

    return{
         "page_content" :build_page_content(course),
         "metadata" : build_metadata(course)
    }