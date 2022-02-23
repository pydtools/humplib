
from humplib import (
    __version__,
    hump2underline,
    json_hump2underline,
    hump_json_renderer_byte,
    hump_json_renderer_str,
)
from humplib import underline2hump
from humplib.tools import json_underline2hump


def test_version():
    assert __version__ == '0.1.5'


def test_underline2hump():
    assert underline2hump("hello_word") == "helloWord"


def test_json_underline2hump():
    data = {
        'name': 'compile',
        'params': {
            'bdg': '1758431528494305280',
            'is_publish': True,
            'token': 'aa.bb.Fx93qRLDHsrQPp8ab1C6Lg4_pnM'
        }
    }

    ret = json_underline2hump(data)
    assert ret == '{"name": "compile","params": {"bdg": "1758431528494305280","isPublish": true,"token": "aa.bb.Fx93qRLDHsrQPp8ab1C6Lg4_pnM"}}'


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
    assert hump_json_renderer_str(data) == '{"a": 1,"aB": 1}'
    assert hump_json_renderer_byte(data) == b'{"a": 1,"aB": 1}'
