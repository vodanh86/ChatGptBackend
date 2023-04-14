import datetime
import json
import urllib.request
import openai
import uuid
from . import utils
from django.http import HttpResponse
from django.conf import settings

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

openai.organization = settings.ORGANIZATION
openai.api_key = settings.API_KEY


@csrf_exempt
def getChat(request):
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
    
    if utils.checkChatCache(preInput, preResponse, question):
        return HttpResponse(utils.checkChatCache(preInput, preResponse, question))

    if choice == 1:
        return HttpResponse(question)
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    if response:
        answer = response["choices"][0]["message"]["content"]

    utils.setChatCache(preInput, preResponse, question, answer)
    print(answer)
    return HttpResponse(answer)

@csrf_exempt
def getImage(request):
    post_data = request.POST
    answer = ""
    choice = 2

    question = post_data.get("text", "")
    if utils.checkImageCache(question):
        return HttpResponse(utils.checkImageCache(question))
    
    response = openai.Image.create(
        prompt=question,
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']

    filename = str(uuid.uuid4()) + ".jpg"
    urllib.request.urlretrieve(image_url, settings.IMAGE_LOCAL + filename)
    print(filename)

    utils.setImageCache(question, settings.IMAGE_PATH + filename)
    print(settings.IMAGE_PATH + filename)
    return HttpResponse(settings.IMAGE_PATH + filename)
