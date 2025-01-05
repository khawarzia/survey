from django.shortcuts import render

def admin_page(request):
    template = 'admin.html'
    context = {}

    return render(request, template, context)

def main_page(request):
    template = 'main.html'
    context = {}
    return render(request, template, context)

def form_page(request,lang):
    if lang == 1:
        template = 'form_arabic.html'
    elif lang == 2:
        template = 'form_english.html'
    elif lang == 3:
        template = 'form_hindi.html'
    else:
        template = 'form_urdu.html'
    context = {}

    if request.method == "POST":
        pass

    return render(request, template, context)

def api_call(request):
    template = 'admin.html'
    context = {}
    return render(request, template, context)