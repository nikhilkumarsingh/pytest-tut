from datetime import datetime

import pytest

from tut6.myapp.student import Student


@pytest.fixture(scope="function")
def dummy_student():
    print("making dummy student")
    return Student("nikhil", datetime(2000, 1, 1), "coe")


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 0
