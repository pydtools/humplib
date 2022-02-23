from humplib import __version__, hump2underline, json_hump2underline, \
    hump_json_renderer
from humplib import underline2hump


def test_version():
    assert __version__ == '0.1.3'


def test_underline2hump():
    assert underline2hump("hello_word") == "helloWord"


def test_hump2underline():
    assert hump2underline("helloWord") == "hello_word"


def test_json_hump2underline():
    json_str = """{"userName":"hi"}"""
    assert json_hump2underline(json_str) == '{"user_name" :"hi"}'


def test_hump_json_renderer():
    data = {
        "a": 1,
        "a_b": 1
    }
    assert hump_json_renderer(data) == b'{"a": 1,"aB": 1}'
