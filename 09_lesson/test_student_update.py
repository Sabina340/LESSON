from models import Student


def test_update_student(db_session):
    student = Student(
        user_id=54321,
        education_form="part-time"
    )
    db_session.add(student)
    db_session.commit()

    student.education_form = "full-time"
    db_session.commit()

    updated_student = (
        db_session.query(Student)
        .filter_by(student_id=student.student_id)
        .first()
    )

    assert updated_student.education_form == "full-time"

    # cleanup
    db_session.delete(updated_student)
    db_session.commit()
