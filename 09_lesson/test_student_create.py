from models import Student


def test_create_student(db_session):
    student = Student(
        user_id=12345,
        education_form="full-time"
    )

    db_session.add(student)
    db_session.commit()

    result = (
        db_session.query(Student)
        .filter_by(user_id=12345)
        .first()
    )

    assert result is not None

    # cleanup
    db_session.delete(result)
    db_session.commit()
