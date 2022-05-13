# Required Envs

| function | variable |
|-|-|
| cancel-booking | BOOKING_TABLE_NAME |
| confirm-booking | BOOKING_TABLE_NAME |
| notify-booking | BOOKING_TOPIC |
| reserve-booking | BOOKING_TABLE_NAME |

See the individual run scripts for local testing.
* [cancel.sh](./cancel.sh)
* [confirm.sh](./confirm.sh)
* [notify.sh](./notify.sh)
* [process.sh](./process.sh)
* [reserve.sh](./reserve.sh)


This is also assuming we have already installed our python invoker.

## Things that didn't work.
Lambda function's `context`. When accessing properties on this object, it blows up. We can work around this by creating a proper mock (or populating the properties for this object). 

`Metrics.log_metric` decorator from `aws_lambda_powertools` (at least in this example) was failing as well.

## Things that did work.






