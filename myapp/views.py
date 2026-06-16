from django.shortcuts import render
import random

def home(request):
    result = ""

    if request.method == "POST":
        names = [
            request.POST["name1"],
            request.POST["name2"],
            request.POST["name3"],
            request.POST["name4"],
            request.POST["name5"],
        ]
        names=[name for name in names if name]
        if names:
            result = random.choice(names)

    return render(request, "myapp/index.html", {'result': result})