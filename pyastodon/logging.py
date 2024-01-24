from __future__ import annotations

import logging
from sys import stderr, stdout


def setupLogging(logLevel: logging._Level) -> None:
    formatter = logging.Formatter(
        fmt = "[%(asctime)s|%(levelname)s|%(name)s]: %(message)s",
        datefmt = "T%H:%M:%S%z",
    )

    stdHandler = logging.StreamHandler(stdout)
    stdHandler.addFilter(lambda l: l.levelno < logging.WARNING)
    stdHandler.setFormatter(formatter)

    errHandler = logging.StreamHandler(stderr)
    errHandler.addFilter(lambda l: l.levelno >= logging.WARNING)
    errHandler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logLevel)
    logger.addHandler(stdHandler)
    logger.addHandler(errHandler)

def getLogger(str) -> logging.Logger:
    return logging.getLogger(f"pyastodon.{str}")