from logic_utils import reset_game_state


def test_new_game_resets_game_state():
    state = {
        "secret": 73,
        "attempts": 4,
        "score": 125,
        "history": [10, 20],
        "status": "won",
        "game_id": 2,
    }

    reset_game_state(state, new_secret=37)

    assert state == {
        "secret": 37,
        "attempts": 0,
        "score": 0,
        "history": [],
        "status": "playing",
        "game_id": 3,
    }
