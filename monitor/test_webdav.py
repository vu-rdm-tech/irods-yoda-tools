import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)


# basic tests
def basic_import_pytest():
    try:
        import pytest

        return True
    except:
        return False


def basic_import_webdavclient3():
    try:
        import webdav3

        return True
    except:
        return False


def basic_import_basic():
    try:
        import json
        import csv
        import requests

        return True
    except:
        return False


# test caller
def test_basic():
    return basic_import_basic


def test_pytest():
    return basic_import_pytest


def test_webdavclient3():
    return basic_import_webdavclient3
