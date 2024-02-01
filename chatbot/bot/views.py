from django.shortcuts import render,redirect
from .forms import MessageForm
from .models import Message,Answer
from django.contrib.auth import logout
import openai
from concurrent.futures import ThreadPoolExecutor
import threading
# Create your views here.

api_key='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'
openai.api_key=api_key
def reply(message):

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=150,
    n=1,
    stop=None,
    temperature=0.7,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{message}"},
    
    ]
    )
    answer=response.choices[0].message.content
    return answer

def home(request):

    messages=Message.objects.filter(user=request.user)
    

    if request.method =='POST':
        form=MessageForm(request.POST)
        
        message=form.save(commit=False)
        message.user=request.user
        message.save()
        with ThreadPoolExecutor() as executor:
            text=executor.submit(reply, request.POST.get('text'))
            answer=Answer(message=message,text=text.result())
            answer.save()
        return redirect('home')
        
        
    else:
       form=MessageForm()
    return render(request,'bot/home.html',{'form':form,'messages':messages})

def logoutPage(request):
    logout(request)
    return redirect('login')