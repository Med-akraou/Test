import openai

# set the API key, replace with your private key the below.
openai.api_key = "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"

model_engine = "text-davinci-002"
prompt = input("tapez votre question")
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text
print(message)