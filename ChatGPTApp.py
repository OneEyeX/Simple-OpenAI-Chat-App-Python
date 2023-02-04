import os

import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

while True:
    prompt=input("\nAsk anything (respecfull OFC!): ")
    completions= openai.Completion.create(prompt=prompt,
        engine='text-davinci-002',
        max_tokens=200
    )
    answer=completions.choices[0].text
    print(answer)