from config import Config
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential


# Uncomment the the model you want to use
model = Config("phi3")
# model = Config("mistral")


# set default values for the client eg max_tokens
client = ChatCompletionsClient(
    endpoint=model.endpoint,
    credential=AzureKeyCredential(model.key),
    max_tokens=100,
)

# Now get model info
model_info = client.get_model_info()

print(f"Model name: {model_info.model_name}")
print(f"Model provider name: {model_info.model_provider_name}")
print(f"Model type: {model_info.model_type}")

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="How many feet are in a mile?"),
    ],
)

print(response.choices[0].message.content)
