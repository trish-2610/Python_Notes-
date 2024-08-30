import logging 

## logging setting 

logging.basicConfig(
    filename = "app1.log",
    filemode = "w",
    level = logging.DEBUG,
)

## create logger 
logger = logging.getLogger("Arithmetic_op")

def add(a,b): 
    logger.debug(f"addition of {a} and {b} = {a+b}")
    return a+b

def sub(a,b): 
    logger.debug(f"subtraction of {a} and {b} = {a-b}")
    return a-b

def mul(a,b): 
    logger.debug(f"multiplication of {a} and {b} = {a*b}")
    return a*b

def div(a,b): 
    try :
        logger.debug(f"addition od {a} and {b} = {a/b}")
        return a/b
    except ZeroDivisionError:
        logger.error("Cannot divide by zero")

add(10,20)
sub(67,45)
mul(3,4)
div(20,0)