from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'ankit',
        'ravi',
        'uttam'
    ]
    # return HttpResponse("<h1>This is home page</h1>")
    return JsonResponse(friends, safe=False)