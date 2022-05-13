from typing import Any
from aws_lambda_powertools.utilities.typing import LambdaContext

from notify_booking.notify import lambda_handler

def notify(req):
  success = lambda_handler(req.get_json(), LambdaContext())
  return "OK" if success else "Unable to notify booking"
