from openai import OpenAI

client = OpenAI(
    base_url={openai_endpoint},
    api_key={auth_key_or_token}
)

response = client.responses.create(
    model={model_deployment},
    instructions="You are a helpful AI assistant.",
    input="Find some information about responsible AI.",
  
    tools=[
        { 
            # A tool definition
            "type": "{tool_type}",
            "{tool-specific-setting}": "{value}",
        },
        { 
            # Another tool definition
            "type": "{another_tool_type}",
            "{tool-specific-setting}": "{value}",
        }
    ]
)
print(response.output_text)