#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import logging
import os
from pathlib import Path

import kanilog
import pytest
import stdlogging
from add_parent_path import add_parent_path

with add_parent_path():
    import wordpress_oauth


logger = kanilog.get_module_logger(__file__, 0)


def setup_module(module):
    pass


def teardown_module(module):
    pass


def setup_function(function):
    pass


def teardown_function(function):
    pass


def test_upload_image():
    image_path = Path(__file__).parent / "images/icon.png"
    api = wordpress_oauth.Wordpress("~/.config/pywordpress_oauth/config.yml")
    __import__('pdb').set_trace()
    result = api.upload_image(image_path)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    kanilog.setup_logger(logfile='/tmp/%s.log' % (os.path.basename(__file__)), level=logging.INFO)
    stdlogging.enable()

    pytest.main([__file__, '-k test_', '-s'])
