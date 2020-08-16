from datetime import datetime

import pytest

from tut8.myapp.student import is_eligible_for_degree


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_is_eligible_for_degree_false(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 19)) is False


def test_student_is_eligible_for_degree_true(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 21)) is True


@pytest.mark.parametrize("credits,expected", [(19, False), (21, True)])
def test_student_is_eligible_for_degree(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student("sam", credits)) is expected


@pytest.mark.parametrize("dummy_student,expected", [(19, False), (21, True)],
                         indirect=["dummy_student"],
                         ids=["ineligible", "eligible"])
def test_student_is_eligible_for_degree(dummy_student, expected):
    assert is_eligible_for_degree(dummy_student) is expected
