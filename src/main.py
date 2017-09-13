# -*- coding: utf-8 -*-
from child import foo
from log import getLogger


logger = getLogger(__name__)


def main():
    logger.debug("msg1")
    print("hello")
    foo()


if __name__ == '__main__':
    main()
