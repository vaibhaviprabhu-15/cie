
def student_details(id,name,course,year):
    result = (
        f"Student ID:{id}\n"
        f"Student name:{name}\n"
        f"Course:{course}\n"
        f"Year:{year}\n"
    )
    return result 
if __name__=="__main__":
    id="101"
    name="vaibhavi"
    course="bca"
    year=2024
    print(student_details(id,name,course,year))
