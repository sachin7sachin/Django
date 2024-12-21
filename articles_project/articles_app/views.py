from django.shortcuts import render

# Create your views here.

dicts = [{
    "id" : 1,
    "name" : "Donald Duck at 90: how the Disney favourite has evolved to appeal to a changing society",
    "description" : "Donald Duck’s first appearance on screen was the animated short titled The Wise Little Hen. He was intended as a one-off supporting character, but his immediate popularity meant Disney used him in subsequent comic stories and animated shorts."
},
{
    "id" : 2,
    "name":"Tom and Jerry – why they’re a cat and mouse double act for the ages",
    "description": "They’ve been part of the backdrop to our lives for so long that it’s easy to forget that – in cat and mouse years anyway – Tom and Jerry’s running conflict must qualify as one of the longest double acts on record. Last month, the pair celebrated their 78th anniversary with the news that they are teaming up in a new animated movie with, of all people, Willy Wonka and his Chocolate factory.",

},
{
    "id" : 3,
    "name" : "Shrek at 20: celebrating the film’s unique brand of animated anarchy and sardonic irreverence",
    "description" : "While Pixar’s groundbreaking Toy Story often achieves plaudits for the shot in the arm it gave Hollywood animation in the mid-1990s, it’s impossible to ignore the influence of DreamWorks’ 2001 computer-animated hit Shrek. The grubbier and more sarcastic sibling to Woody and Buzz, Shrek was a milestone for American cartoons that paved the way for a unique brand of animated anarchy and sardonic irreverence that still holds sway across the industry today."
}
]


def home(request):

    search = request.GET.get("search")
    result = dicts

    if search:
        result = [
            i for i in result
                if search.lower() in i["name"].lower()
                ]
        
    context = {
        "title" : "home page",
        "search":search,
        "dict" : result
    }
    return render(request,"home.html",context)

def about(request):
    context = {
        "title" : "about page"
    }
    return render(request,"about.html",context)

def contact(request):
    context = {
        "title" : "contact page"
    }
    return render(request,"contact.html",context)

def task(request,id):
    data = None

    for i in dicts:
        if i["id"] == id:
            data = i
            break
    context = {
        "task" : data
    }
    return render(request, 'task.html',context)
    
        

