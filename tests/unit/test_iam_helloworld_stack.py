import aws_cdk as core
import aws_cdk.assertions as assertions

from iam_helloworld.iam_helloworld_stack import IamHelloworldStack

# example tests. To run these tests, uncomment this file along with the example
# resource in iam_helloworld/iam_helloworld_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IamHelloworldStack(app, "iam-helloworld")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
