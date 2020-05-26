def add_2(number: float):
    """A function that adds 2 to any number provided."""
    return number + 2


def say_hello():
    """Helper function for lambda_handler."""
    return "Hello World!"


def lambda_handler(event, context):
    """The main lambda handler."""
    return {
        'statusCode': 200,
        'body': say_hello()
    }
