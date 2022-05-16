# Converting an AWS Lambda Example to TAP

We will be attemting to port the [AWS Lambda example](https://github.com/aws-samples/aws-serverless-airline-booking) to TAP functions. We will only be migrating the `booking` backend section.

**NOTE** I was unsuccessful trying to deploy this to AWS Amplify. If you can get it to successfully deploy, it'll save you a bunch of manual work in setting up the relevant AWS backends needed to make this function correctly.

## Prerequisites
To begin, we will need to set up a few things.

### DynamoDB
This is where the flight bookings and flight are stored.
From the AWS DynamoDB page follow the prompts to create 2 tables
* Flights
* Bookings

### AWS AppSync
This is how we will be accessing the database to create the API layer for accessing our database.

### AWS Cognito
This manages the users for accessing the API
* Important group:
    * `Admin`: This group allows access to bookings and flights

## Next Steps
We need to first do what AWS Lambda does with layers. We will combine the layered dependencies into the same folder of the project. In this case, the `src/backend/shared/lib/process_booking` needs to live in `src/backend/booking/src` folder.

Once this folder has been moved. We will then rename all the folders under `src/backend/booking/src` from `*-booking` to `*_booking`. We will be using the src folder here as the root of where our function will live.

By inspecting the code, we see that `context` in the Lambda function handler is not used directly. A few of the tools installed by `aws_lambda_powertools` module uses the context object under the hood, but they were mostly for logging and tracing. We ended up removing these decorators.

At this point we can create a wrapper for the `lambda_handler`. We start by creating a file for the function we want. Let's take `cancel_booking` for example. We'll create a file (module) called `cancel.py`. Within the file we will import the Lambda handler from the `cancel_booking` package.
```
from cancel_booking.cancel import lambda_handler
```

Additionally, we need to pass in a `LambdaContext` to the method so we'll import that too.

```
from aws_lambda_powertools.utilities.typing import LambdaContext
```

Our Python invoker expects specific names for the function parameters. In this case we'll be working as an HTTP function. So we'll use `req` as the parameter. In the body of the function, we'll forward the request to the lambda handler. We'll define a function like so:
```
def cancel(req):
    success = lambda_handler(req.get_json(), LambdaContext())
    return "OK" if success else "Unable to cancel booking"
```
Of course the return is up to you what you want to return.

In the cases where some of the decorators that do use `LambdaContext`, it fails because it can't access the properties. We could mock or populate the context in the `cancel` function we defined.

The alternative is to strip out the pieces that rely on `LambdaContext`.

---

## Thoughts/Lessons learned

### Functions might live in one mono-repo.
* Buildpacks might need to have a way to configure the location of the functions.

### Response codes for http functions
* The only way to do this currently is to return a `Flask.response` object.
* We may instead want to return a tuple `(code, body)` or just the body and let the invoker decide the status code.
