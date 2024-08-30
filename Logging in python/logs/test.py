from logger import logging

def add(a,b):
    logging.debug("This is an addition operation")
    return a+b

logging.info("This is an info message ")
add(2,3)