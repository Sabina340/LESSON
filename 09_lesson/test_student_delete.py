from models import Student


def test_delete_student(db_session):
    student = Student(
        user_id=99999,
        education_form="distance"
    )
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    deleted_student = (
        db_session.query(Student)
        .filter_by(student_id=student.student_id)
        .first()
    )

    assert deleted_student is None
