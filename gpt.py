import openai

def ai(prompt):
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0,
                                        max_tokens=2500)
    
    return response.choices[0].text