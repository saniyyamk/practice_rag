from pathlib import Path
import json

from normalizer import normalize_course


DATA_DIR = Path(__file__).resolve().parent.parent/ "data"

def discover_json_files():
    json_files = list(DATA_DIR.rglob("*.json"))
    return json_files


def load_json_file(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        return json.load(file)

def inspect_course_structure(course):
    print("\nCourse structure")
    print("--"*20)
    for key,value in course.items():
        print(f"{key}; {type(value).__name__}")

def inspect_dataset():

    files= discover_json_files()

    total_courses = 0

    for file_path in files:

        data = load_json_file(file_path)

        if isinstance(data,list):
            total_courses +=len(data)

            if data:
                print(f"\nFILE: {file_path.name}")
                inspect_course_structure(data[0])

    print("\nTotal courses :",total_courses)


def load_all_courses():
    courses =[]

    json_files=discover_json_files()
    for file_path in json_files:
        data=load_json_file(file_path)

        if isinstance(data,list):
            record=data
        elif isinstance(data,dict):
            record= [data]

        else:
            print(f"{file_path} unsupported format")

            continue
        for course in record:
            normalized_course = normalize_course(
                course=course,
                source_file=file_path.name,
                source_path=str(file_path.relative_to(DATA_DIR))

            )

            courses.append(normalized_course)

    return courses

def validate_courses(courses):

    required_fields =[
        "course_name",
        "course_category",
        "department",
        "objective",
        "course_outline"
    ]

    print("\n" + "=" *60)
    print("DATA VALIDATION")
    print("=" * 60)

    for field in required_fields:

        missing =sum(
            1
            for course in courses
            if not course.get(field)
        )

        print(f"{field:<20}: {missing} missing")

    duration_months = sum(
        1
        for course in courses
        if course["duration"]["months"] is not None
    )

    duration_hours = sum(
        1
        for course in courses
        if course["duration"]["hours"] is not None
    )


    print()
    print(f"Duration with months : {duration_months}")
    print(f"Duration with hours :{duration_hours}")


if __name__ == "__main__":
    courses= load_all_courses()

    print("="*60)
    print("INGESTION RESULT")
    print("="*60)

    print(f"JSON files : {len(discover_json_files())}")
    print(f"Courses    :{len(courses)}")

    validate_courses(courses)
    print("First course:")

    print(courses[0])