from django.shortcuts import render
from .models import FoodModel
from .forms import FoodForm
# Create your views here.
def home(request, methods=["GET"]):
    foods = FoodModel.objects.all()
    return render(request, "main/index.html", {"foods":foods})

def post(request):
    foods = FoodModel.objects.all()

    
    form = FoodForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
    return render(request, "main/post.html", {"form": form,  "foods" : foods})
