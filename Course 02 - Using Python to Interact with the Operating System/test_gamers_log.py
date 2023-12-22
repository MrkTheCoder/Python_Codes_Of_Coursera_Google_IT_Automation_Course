import unittest
from unittest.mock import patch, mock_open
from gamers_log import parse_log_file


class TestGamersLog(unittest.TestCase):

    def test_parse__log_file_with_one_correct_log_line_without_rank_should_return_tables(self):
        mock_file_contents = "[2023/12/15] [12:40 PM]: LOSE any game (MockUser1)"
        mock_file_path = "mock/file/path"

        with patch('gamers_log.open', new=mock_open(read_data=mock_file_contents)) as _file:
            players, games = parse_log_file(mock_file_path)
            _file.assert_called_once_with(mock_file_path)
        expected_players = [('MockUser1', 0, 1)]
        expected_games = [('any game', 1)]

        self.assertEqual(players, expected_players)
        self.assertEqual(games, expected_games)


if __name__ == '__main__':
    unittest.main()
