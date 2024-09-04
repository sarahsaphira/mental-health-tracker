from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306240093',
        'name': 'Sarah Saphira Setiawan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)