from student import student_details
def test_student_details():
    expected_output = (
        "Student ID:101\n"
        "Student name:vaibhavi\n"
        "Course:bca\n"
        "Year:2024\n"
    )
    assert student_details("101", "vaibhavi", "bca", 2024) == expected_output
