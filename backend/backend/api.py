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
    preInput = post_data.get("preInput", "")
    preResponse = post_data.get("preResponse", "")
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": preInput},
            {"role": "assistant", "content": preResponse},
            {"role": "user", "content": question}
        ]
    print(messages)

    if choice == 1:
        return HttpResponse(question)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    if response:
        answer = response["choices"][0]["message"]["content"]
        
    print(answer)
    return HttpResponse(answer)
