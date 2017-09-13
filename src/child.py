# -*- coding: utf-8 -*-
from logging import getLogger, FileHandler, DEBUG, basicConfig


logger = getLogger(__name__)
basicConfig(level=DEBUG)

fh = FileHandler('log.log', 'a+')
fh.level = DEBUG
logger.addHandler(fh)


def foo():
    logger.debug("msg foo1")
    print("child foo 1")
