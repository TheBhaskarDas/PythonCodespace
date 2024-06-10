def dictionary_comprehension():
    names = ['collin', 'alex', 'kanman', 'sampark', 'danish', 'lessie', 'prerna', 'manoj', 'sounak', 'grasim']
    import random
    students_score = {student_keys: random.randint(1, 100) for student_keys in names}
    passed_students = {student_keys: b for (student_keys, b) in students_score.items() if b >= 55}
    print(f"passed students are:  + {passed_students}")

    failed_students = {student_keys: score for (student_keys, score) in students_score.items() if score < 55}
    print(f"failed students are:  + {failed_students}")


dictionary_comprehension()
