import pytest

from tut2.myapp.sample import validate_age


def test_validate_age_valid_age():
    validate_age(10)


def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)
