import pytest

from logic_utils import check_guess, get_guess_message


@pytest.mark.parametrize(
    ("guess", "secret", "expected_message"),
    [
        (19, 18, "📉 Go LOWER!"),
        (17, 18, "📈 Go HIGHER!"),
    ],
)
def test_guess_hint_direction(guess, secret, expected_message):
    outcome = check_guess(guess, secret)
    assert get_guess_message(outcome) == expected_message
