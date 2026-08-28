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

        module = item.get("module")
        title = item.get("title")
        topics =item.get("topics",[])

        if isinstance(module,str):

            module_title = module

            curriculum_text = (
                f"Module : {module_title}"
            )

        else:

            module_title =title or f"Module {index}"

            curriculum_text = (
                f"Module {module} : {module_title}" 
            )

        if isinstance(topics,list) and topics:

            curriculum_text +="\n Topics:\n"

            for topic in topics:
                curriculum_text += f"- {topic}\n"

        page_content =f"""
Course :{course['course_name']}

Department : {course['department']}

Category : {course['course_category']}

{curriculum_text}
""".strip()

        metadata= {
            "document_type" :"module",
            "course_name" :course["course_name"],
            "department" : course["department"],
            "course_category" :course["course_category"],
            "duration_months" :course["duration"]["months"],
            "duration_hours" :course["duration"]["hours"],
            "module_index" : index,
            "source_file" :course["source"]["file"],
            "source_path" :course["source"]["path"]
        }

        chunks.append({
            "page_content" : page_content,
            "metadata" : metadata
        })

    return chunks