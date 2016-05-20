# coding=utf-8
from __future__ import absolute_import


def deep_get(d, path):
    """Get value given the dictionary and path

    If there is a value we can find along the path, return it.
    Otherwise, return None.

    :param d:
    :type d: dict
    :param path:
    :type path: list
    :return:
    :rtype:
    """
    assert isinstance(d, dict)
    assert isinstance(path, list)
    return _get_value_from_dict(d, path)


def _get_value_from_dict(d, path):
    if d is None:
        return None
    if len(path) == 0:
        return d
    if isinstance(path[0], str):
        next_value = d.get(path[0])
        if len(path) == 1:
            return next_value
        if isinstance(next_value, dict):
            return _get_value_from_dict(next_value, path[1:])
        if isinstance(next_value, list):
            return _get_value_from_list(next_value, path[1:])
        return None
    return None


def _get_value_from_list(l, path):
    if l is None or len(l) == 0:
        return None
    if len(path) == 0:
        return l
    if isinstance(path[0], int):
        if path[0] >= len(l) or -path[0] > len(l):
            return None
        next_value = l[path[0]]
        if len(path) == 1:
            return next_value
        if isinstance(next_value, dict):
            return _get_value_from_dict(next_value, path[1:])
        if isinstance(next_value, list):
            return _get_value_from_list(next_value, path[1:])
        return None
    return None
