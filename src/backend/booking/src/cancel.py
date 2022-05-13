from sys import maxsize
from typing import Any
from aws_lambda_powertools.utilities.typing import LambdaContext

from cancel_booking.cancel import lambda_handler

def cancel(req):
  success = lambda_handler(req.get_json(), LambdaContext())
  return "OK" if success else "Unable to cancel booking"
