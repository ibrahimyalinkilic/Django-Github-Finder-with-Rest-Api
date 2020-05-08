from django.shortcuts import render, HttpResponse
import requests
from django.contrib import messages

def index(request):
    
    base_url = "https://api.github.com/users/"
    if request.POST:
        githubname = request.POST.get("githubname")
        response = requests.get(base_url + githubname)
        response_repos = requests.get(base_url + githubname + "/repos")
        
        user_info = response.json()
        repos = response_repos.json()
        if "message" in user_info:

            messages.success(request,"Böyle bir kullanıcı bulunmamaktadır.")
            return render(request,"index.html")

        return render(request,"index.html",{"profile":user_info,"repos":repos})
    else:
        return render(request, "index.html")
