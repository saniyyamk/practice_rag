import re

def normalization_duration(duration):

    result={
        "raw":duration,
        "months":None,
        "hours":None
    }

    if isinstance(duration,dict):
        print('hited')
        result["months"] = duration.get("months")
        result["hours"] = duration.get("hours")
        
        return result

    if isinstance(duration,str):
        month_match = re.search(
            r"(\d+(?:\.\d+)?)\s*months?",
            duration,
            re.IGNORECASE
        )

        hour_match = re.search(
                    r"(\d+(?:\.\d+)?)\s*hours?",
                    duration,
                    re.IGNORECASE
                )
        if month_match:
            result["months"] = float(month_match.group(1))

        if hour_match:
                result["hours"] = float(hour_match.group(1))
    
    return result


def normalize_course(course,source_file,source_path):
    normalized ={
          "course_name":course.get("course_name"),
          "course_category":course.get("course_category"),
          "department":course.get("department"),
          "duration":normalization_duration(
               course.get("course_duration")
          ),
          "course_outline":course.get("course_outline",[]),
          "objective":course.get("objective"),
          "duration_details": course.get("duration_details"),
          "source":{
                 "file": source_file,
                 "path": source_path
            }

        

        }
    
    return normalized



