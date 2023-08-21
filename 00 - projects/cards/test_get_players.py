import mock

from players import get_players
from test_config import PLAYER1, PLAYER2
from config import black_list


def mock_inputs(prompt):
    return next(names)


names = (name for name in [PLAYER1, PLAYER2])
with mock.patch('builtins.input', mock_inputs):
    assert get_players(2) == [[PLAYER1, []], [PLAYER2, []]]


names = (name for name in [PLAYER1, black_list[0], PLAYER2])
with mock.patch('builtins.input', mock_inputs):
    with mock.patch('builtins.print') as mocked_print:
        assert get_players(2) == [[PLAYER1, []], [PLAYER2, []]]
        assert mocked_print.mock_calls == [mock.call('Игрок в чёрном списке')]


names = (name for name in [PLAYER1, PLAYER1, PLAYER2])
with mock.patch('builtins.input', mock_inputs):
    with mock.patch('builtins.print') as mocked_print:
        assert get_players(2) == [[PLAYER1, []], [PLAYER2, []]]
        assert mocked_print.mock_calls == [mock.call('Игрок уже добавлен')]
