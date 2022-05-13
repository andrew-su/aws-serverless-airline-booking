from typing import Any
from aws_lambda_powertools.utilities.typing import LambdaContext

from reserve_booking.reserve import lambda_handler

def reserve(req):
  success = lambda_handler(req.get_json(), LambdaContext())
  return "OK" if success else "Unable to reserve booking"
