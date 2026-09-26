from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

# Get response using the code_interpreter tool
response = client.responses.create(
    model={model_deployment},
    instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
    input="What is the square root of 16?",
    tools=[{"type": "code_interpreter",
            "container": {"type": "auto"}}]
)
print(response.output_text)