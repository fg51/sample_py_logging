# -*- coding: utf-8 -*-
import os.path
import logging
from logging import config
from logging import FileHandler, WARN, basicConfig

from typing import List, Optional  # NOQA  # pylint: disable=W0611


class Globals(object):
    is_file = None      # type: bool
    is_needed = True    # type: bool
    config_path = "logging.conf"
    __slot__ = []   # type: List[str]


if Globals.is_file is None:
    Globals.is_file = os.path.isfile(Globals.config_path)

if Globals.is_file:
    if Globals.is_needed:
        Globals.is_needed = False
        config.fileConfig(Globals.config_path)
else:
    if Globals.is_needed:
        Globals.is_needed = False
        basicConfig(level=WARN)


def set_log_config_path(filepath):
    # type: (Optional[str]) -> None
    if filepath:
        if os.path.isfile(filepath):
            Globals.is_needed = True
            Globals.config_path = filepath


def getLogger(name):
    # type: (str) -> logging.Logger

    if Globals.is_file is None:
        Globals.is_file = os.path.isfile(Globals.config_path)

    if Globals.is_file:
        if Globals.is_needed:
            Globals.is_needed = False
            config.fileConfig(Globals.config_path)
        return logging.getLogger(name)

    if Globals.is_needed:
        Globals.is_needed = False
        basicConfig(level=WARN)
    logger = logging.getLogger(name)
    fh = FileHandler('log.log', 'a+')
    logger.addHandler(fh)
    return logger
