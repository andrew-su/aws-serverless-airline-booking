#!/usr/bin/env bash

export BOOKING_TOPIC='arn:aws:sns:us-east-1:612314536519:airline'
export MODULE_NAME=notify
export FUNCTION_NAME=notify

python -m pyfunc start
