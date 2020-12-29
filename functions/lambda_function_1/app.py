from lambda_common_code.status import *

def lambda_handler(event, context):
    return status(200, "OK")
