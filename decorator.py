import logging

def dec_with_params(message):
    def dec_function(function):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger("testDec")
            logger.setLevel(logging.DEBUG)
            logger.addHandler(logging.StreamHandler())
            logger.info("This is just testing message from decarator ")
            logger.info(message)
            return function()
        return wrapper
    return dec_function

@dec_with_params("Messages is dummy")
def test_funt():
    print("this is in test fucntoin ")
    return "test funct"

@dec_with_params("Messages is  not dummy")
def test_funt2():
    print("this is in test fucntoin second ")
    return "test funct secind"

if __name__ == "__main__":
    print(test_funt())
    print(test_funt2())
