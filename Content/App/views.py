from django.shortcuts import render
import openai
import os
from django.http import HttpResponse
from .content_generator import generateBlogTopics
# Create your views here.

openai.api_key = "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"

def home(request):
    blogTopicIdeas= None
    if request.method == "POST":
        prompt = request.POST.get('blogTopic')
        blogT = generateBlogTopics(prompt)
        blogTopicIdeas = blogT.replace('\n','<br>')
        print(blogTopicIdeas,"This is blogTopic")
    return render(request,'app/home.html',{'blogtopicidead':blogTopicIdeas})







# def Content_generator(request):
#     response = openai.Completion.create(model="text-davinci-003", prompt="Neeraj", temperature=0, max_tokens=100)
#     print(response,"THis is responce")
#     return HttpResponse(response)




#BACK UP
# def Content_generator(request):
#     openai.api_key = "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"
#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt="Mahara",
#     temperature=0.7,
#     max_tokens=917,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )
#     print(response['choices'],"THIS IS INSIDE OF CHICES")
#     choice = response['choices']
#     print(choice,"dfs")
#     # print(choice[finish_reason],"STOP")
#     # print(response,"THIS IS RESPONSE")
#     context = {
#         'response_choice':response['choices'][{finish_reason}],
#     }
#     return render(request,'app/home.html',context)