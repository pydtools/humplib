#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
doc:
"""
import json
import re

from humplib.dumps import dumps


pattern_hump2under = re.compile(r'"\s*(\w+)\s*"\s*:')
pattern_json_under2hump = re.compile(r'(_\w+\":)')


def str_to_json(s):
    if not s:
        return None
    return json.loads(s)


def hump2underline(hump_str):
    """
    驼峰形式字符串转成下划线形式
    :param hump_str: 驼峰形式字符串
    :return: 字母全小写的下划线形式字符串
    """
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 这里第二个参数使用了正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hump_str).lower()
    return sub


def underline2hump(underline_str, code='utf8'):
    """
    下划线形式字符串转成驼峰形式
    :param underline_str: 下划线形式字符串
    :param code: utf8
    :return: 驼峰形式字符串
    """
    if isinstance(underline_str, bytes):
        underline_str = underline_str.decode(code)
    # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，
    # 回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
    sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), underline_str)
    return sub


def key_to_upper(x):
    """
    x.group(1)[0] 是"_"

    :param x:
    :return:
    """
    n = x.group(1)[1:]
    return str(n).capitalize()


def json_str_underline2hump(json_str: str=None)->str:
    """
    json snake -> hump

    匹配所有的json key中包含下划线开始的键以":结尾

    :param json_str: 标准json 不使用单引号和nan
    :return:
    """
    # return re.sub(r"(_\w+\":)", key_to_upper, json_str)
    return re.sub(pattern_json_under2hump, key_to_upper, json_str)


def json_underline2hump(json_obj: dict=None)->str:
    """
    json snake -> hump

    匹配所有的json key中包含下划线开始的键以":结尾

    :param json_obj: 标准json 不使用单引号和nan
    :return:
    """
    json_str = dumps(json_obj)
    return json_str_underline2hump(json_str=json_str)


def json_hump2underline(hump_json_str, code='utf8'):
    """
    把一个json字符串中的所有字段名都从驼峰形式替换成下划线形式。
    注意点：因为考虑到json可能具有多层嵌套的复杂结构，
    所以这里直接采用正则文本替换的方式进行处理，而不是采用把json转成字典再进行处理的方式
    :param hump_json_str: 字段名为驼峰形式的json字符串
    :param code: utf8
    :return: 字段名为下划线形式的json字符串
    """
    if isinstance(hump_json_str, bytes):
        hump_json_str = hump_json_str.decode(code)
    # 从json字符串中匹配字段名的正则
    # 注：这里的字段名只考虑由英文字母、数字、下划线组成
    # attr_ptn = re.compile(r'"\s*(\w+)\s*"\s*:')
    # 使用hump2underline函数作为re.sub函数第二个参数的回调函数
    sub = re.sub(
        pattern_hump2under, lambda x: '"' + hump2underline(x.group(1)) +
                            '" :', hump_json_str)
    return sub
