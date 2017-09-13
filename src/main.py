# -*- coding: utf-8 -*-
from logging import getLogger, FileHandler, DEBUG, basicConfig
from child import foo

logger = getLogger(__name__)
basicConfig(level=DEBUG)

fh = FileHandler('log.log', 'a+')
fh.level = DEBUG
logger.addHandler(fh)


def main():
    logger.debug("msg1")
    print("hello")
    foo()


if __name__ == '__main__':
    main()
