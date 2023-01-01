import os
import openai


def generateBlogTopics(prompt):
    openai.api_key = "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"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Generate blog topics on:{}. \n \n 1.".format(prompt),
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    return response['choices'][0]['text']

