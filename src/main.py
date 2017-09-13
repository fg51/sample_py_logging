# -*- coding: utf-8 -*-
from log import getLogger

from child import foo

logger = getLogger(__name__)


def main():
    logger.debug("msg1")
    print("hello")
    foo()


if __name__ == '__main__':
    main()
