import datetime
import json
import openai
from django.http import HttpResponse
from django.conf import settings

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

openai.organization = settings.ORGANIZATION
openai.api_key = settings.API_KEY


@csrf_exempt
def getResult(request):
    post_data = request.POST
    answer = ""
    choice = 2

    question = post_data.get("text", "")
    print(post_data)
    print(question)

    if choice == 1:
        return HttpResponse(question)
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=question,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": "Who won the world series in 2020?"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": question}
        ]
    )
    if response:
        answer = response["choices"][0]["message"]["content"]
    print(answer)
    return HttpResponse(answer)
