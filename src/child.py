# -*- coding: utf-8 -*-
from log import getLogger


logger = getLogger(__name__)


def foo():
    logger.debug("msg foo1")
    print("child foo 1")
