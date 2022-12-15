from django.shortcuts import render
# Import necessary modules and libraries
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Import the chatbot model and functions
from chatbot_model import predict, train


# Create your views here.


from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



@csrf_exempt
def chatbot_view(request):
    # Parse the JSON data from the request
    data = json.loads(request.body)
    
    # Get the user input from the request data
    user_input = data['user_input']
    
    # Use the chatbot model to generate a response
    response = predict(user_input)
    
    # Return the response as a JSON object
    return HttpResponse(json.dumps({'response': response}), content_type='application/json')
