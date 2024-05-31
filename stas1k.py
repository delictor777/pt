# klicsk-fpZuHWFtBJjDbU1YzXeCT3BlbkFJRy9f2IXhtBsvDjkDWgQK
# 'klicsk-Q7EvSsXP89XjZKDRHUq8T3BlbkFJVmNrKlzZKFDwnihxkQwv'

import openai

openai.api_key = 


def get_response_from_chatgpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)

prompt = input('you: ')
response = get_response_from_chatgpt(prompt)
print(response)


