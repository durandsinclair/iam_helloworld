from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
from constructs import Construct
from pathlib import Path

class IamHelloworldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "IamHelloworldQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # Define the lambda function
        lambda_function = _lambda.Function(
            self, "HelloWorldLambda",
            runtime = _lambda.Runtime.PYTHON_3_10,
            handler = "index.handler",
            code = _lambda.Code.from_inline(
                """
def handler(event, context):
    # print("Event:", json.dumps(event)) 
    return {
        'statusCode': 200,
        'body': 'Hello World!'
    }"""
            )
        )

        # Define the API Gateway 
        api = apigateway.LambdaRestApi(
            self, "HelloWorldApi",
            handler = lambda_function,
            description="API Gateway for HelloWorld Lambda",
        )

        # Create IAM user with restricted permissions
        iam_user = iam.User(
            self, "HelloWorldUser",
            user_name = "userName"
        )

        # Attach policy to allow invoking the API Gateway
        api_invoke_policy = iam.Policy(
            self, "ApiInvokePolicy",
            statements = [
                iam.PolicyStatement(
                    actions=["execute-api:Invoke"],
                    resources=[f"{api.arn_for_execute_api()}/*"]
                )
            ]
        )
        iam_user.attach_inline_policy(api_invoke_policy)


