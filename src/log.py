# -*- coding: utf-8 -*-
import logging
from logging import FileHandler, WARN, basicConfig


def getLogger(name):
    logger = logging.getLogger(name)
    basicConfig(level=WARN)

    fh = FileHandler('log.log', 'a+')
    fh.level = WARN
    logger.addHandler(fh)
    return logger
