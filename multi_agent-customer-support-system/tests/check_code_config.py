import boto3

client = boto3.client(
    "bedrock-agentcore-control",
    region_name="us-east-1"
)

shape = (
    client.meta.service_model
    .operation_model("CreateAgentRuntime")
    .input_shape
    .members["agentRuntimeArtifact"]
    .members["codeConfiguration"]
)

print(shape)
print(shape.members.keys())