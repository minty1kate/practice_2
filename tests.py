import pytest
from unittest import mock
from main import bruteforce, with_dict

@pytest.mark.parametrize("words, ans, length", [
    (["abcab", "abcd"], ("abcab", "abcd"), 2),
    (["abc", "def"], None, 0),
    ([], None, 0),
])
def test_bruteforce_logic(words, ans, length):
    data = "\n".join(words)
    with mock.patch("builtins.open", mock.mock_open(read_data=data)):
        res_ans, res_len = bruteforce("test.txt")
        assert res_ans == ans
        assert res_len == length

@pytest.mark.parametrize("words, ans, length", [
    (["abcab", "abcd"], ("abcab", "abcd"), 2),
    (["abc", "def"], None, 0),
    ([], None, 0),
])
def test_with_dict_logic(words, ans, length):
    data = "\n".join(words)
    with mock.patch("builtins.open", mock.mock_open(read_data=data)):
        res_ans, res_len = with_dict("test.txt")
        assert res_ans == ans
        assert res_len == length


@pytest.mark.parametrize("func", [bruteforce, with_dict])
def test_type_error(func):
    with pytest.raises(TypeError):
        func(None)


def test_mock_vs_magic():
    mocked_instance = mock.Mock()
    magic_instance = mock.MagicMock()

    mocked_instance.__str__ = mock.Mock(return_value="Mock")
    magic_instance.__str__.return_value = "Magic"

    assert str(mocked_instance) == "Mock"
    assert str(magic_instance) == "Magic"




