import unittest
from unittest.mock import patch, mock_open
from gamers_log import parse_log_file


class TestGamersLog(unittest.TestCase):

    def test_parse_log_file_with_one_correct_log_line_without_rank_should_return_tables(self):
        mock_file_contents = "[2023/12/15] [12:40 PM]: LOSE any game (MockUser1)"
        mock_file_path = "mock/file/path"
        expected_players = [('MockUser1', 0, 1)]
        expected_games = [('any game', 1)]

        with patch('gamers_log.open', new=mock_open(read_data=mock_file_contents)) as _file:
            players, games = parse_log_file(mock_file_path)
            _file.assert_called_once_with(mock_file_path)

        self.assertEqual(players, expected_players)
        self.assertEqual(games, expected_games)

    def test_parse_log_file_with_one_correct_log_line_with_rank_should_return_tables(self):
        mock_file_contents = "[2023/12/15] [12:40 PM]: WIN game v2 #72 (Mock_User)"
        mock_file_path = "mock/file/path"
        expected_players = [('Mock_User', 1, 0)]
        expected_games = [('game v2', 1)]

        with patch('gamers_log.open', new=mock_open(read_data=mock_file_contents)) as _file:
            players, games = parse_log_file(mock_file_path)
            _file.assert_called_once_with(mock_file_path)

        self.assertEqual(players, expected_players)
        self.assertEqual(games, expected_games)

    def test_parse_log_file_with_one_wrong_log_line_should_return_empty_tables(self):
        mock_file_contents = "[2023/12/15] [12:40 PM]: Info game #72 (Mock_User)"
        mock_file_path = "mock/file/path"
        expected_players = []
        expected_games = []

        with patch('gamers_log.open', new=mock_open(read_data=mock_file_contents)) as _file:
            players, games = parse_log_file(mock_file_path)
            _file.assert_called_once_with(mock_file_path)

        self.assertEqual(players, expected_players)
        self.assertEqual(games, expected_games)

    def test_parse_log_file_with_empty_log_should_return_empty_tables(self):
        mock_file_contents = ""
        mock_file_path = "mock/file/path"
        expected_players = []
        expected_games = []

        with patch('gamers_log.open', new=mock_open(read_data=mock_file_contents)) as _file:
            players, games = parse_log_file(mock_file_path)
            _file.assert_called_once_with(mock_file_path)

        self.assertEqual(players, expected_players)
        self.assertEqual(games, expected_games)

    def test_parse_log_file_with_multiple_lines_should_return_tables(self):
        mock_file_contents = """[2023/12/15] [12:40 PM]: WIN game v2 #72 (Mock_User)
[2023/12/15] [12:40 PM]: WIN NiceGame (AceUser)
[2023/12/15] [12:40 PM]: LOSE game v2 #72 (Mock_User)
[2023/12/15] [12:40 PM]: LOSE any game #72 (Mock_User)"""
        mock_file_path = "mock/file/path"
        expected_players = [('AceUser', 1, 0), ('Mock_User', 1, 2)]
        expected_games = [('game v2', 2), ('NiceGame', 1), ('any game', 1)]

        with patch('gamers_log.open', new=mock_open(read_data=mock_file_contents)) as _file:
            players, games = parse_log_file(mock_file_path)
            _file.assert_called_once_with(mock_file_path)

        self.assertEqual(players, expected_players)
        self.assertEqual(games, expected_games)


if __name__ == '__main__':
    unittest.main()
