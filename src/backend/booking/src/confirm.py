from typing import Any
from aws_lambda_powertools.utilities.typing import LambdaContext

from confirm_booking.confirm import lambda_handler

def confirm(req):
  success = lambda_handler(req.get_json(), LambdaContext())
  return "OK" if success else "Unable to confirm booking"
