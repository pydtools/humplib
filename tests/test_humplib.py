from humplib import __version__, hump2underline, json_hump2underline
from humplib import underline2hump


def test_version():
    assert __version__ == '0.1.2'


def test_underline2hump():
    assert underline2hump("hello_word") == "helloWord"


def test_hump2underline():
    assert hump2underline("helloWord") == "hello_word"


def test_json_hump2underline():
    json_str = """{"userName":"hi"}"""
    assert json_hump2underline(json_str) == '{"user_name" :"hi"}'
