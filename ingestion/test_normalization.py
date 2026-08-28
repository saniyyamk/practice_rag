from normalizer import normalize_course

course= {
    "course_name":"Example Course",
    "course_category":"Certificate Course",
    "department" : "CAD",

    "course_duration" :{
        "hours" : 72,
        "months":2
    },

    "objective" : "Example objective",

    "course_outline":[
        {
            "module":"Introduction"
        }
    ]
}


result =normalize_course(
    course,
    "example.json",
    "CAD/example.json"
)

print(result)