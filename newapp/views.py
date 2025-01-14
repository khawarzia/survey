from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import form_submission, api_keys
from django.contrib.auth.models import User
from django.contrib import auth
import json

def admin_page(request):
    template = 'admin.html'
    context = {}

    if not request.user.is_authenticated:
        return redirect("/admin/")
    
    context['data'] = form_submission.objects.all()

    return render(request, template, context)

def admin_login_page(request):
    template = 'login.html'
    context = {}

    if request.user.is_authenticated:
        return redirect("/admin-page/")
    
    if request.method == "POST":
        try:
            obj = User.objects.get(username=request.POST['name'])
            if obj.check_password(request.POST['pass']):
                auth.login(request,obj)
                return redirect("/admin-page/")
            else:
                context['msg'] = "Please enter valid credentials!"
        except:
            context['msg'] = "Please enter valid credentials!"

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
        obj = form_submission()
        obj.form_type = request.POST['look']
        obj.name = request.POST['name']
        obj.phone_number = request.POST['phone']
        obj.comments = request.POST['comments']
        if request.POST['typeof'] in ('1','2','3','4','5','6'):
            obj.property_type = request.POST['typeof']
            if request.POST['typeof'] == '2':
                obj.apartment_type = request.POST['size']
        else:
            obj.property_type = request.POST['otherprop']
        obj.fav_district = request.POST['dist']
        if request.POST['look'] == "1":
            obj.purpose = request.POST['purpose']
        obj.save()

        return redirect('/success/{}'.format(lang))

    return render(request, template, context)

def success_page(request,lang):
    template = 'main.html'
    context = {}
    if lang == 1:
        context['msg'] = "تم إرسال الطلب بنجاح"
    elif lang == 2:
        context['msg'] = "Request submitted successfully"
    elif lang == 3:
        context['msg'] = "अनुरोध सफलतापूर्वक सबमिट किया गया"
    else:
        context['msg'] = "درخواست کامیابی کے ساتھ جمع کرادی گئی۔"
    return render(request, template, context)

def api_call(request,key):
    context = {}

    objs = api_keys.objects.filter(api_key=key)
    if (len(objs) > 0 and objs[0].allowed):
        context['response'] = "Success"
        data_list = []
        for i in form_submission.objects.all():
            temp_obj = {'date':str(i.submission_date), 
                        'name': i.name, 
                        'phone': i.phone_number,
                        'looking-for': i.getFormType(),
                        'property-type': i.getPropertyType(),
                        'apartment-type': i.getApartmentType(),
                        'favorite-district': i.fav_district,
                        'renting-reason': i.getPurpose(),
                        'comments': i.comments
            }
            data_list.append(temp_obj)
        context['data'] = data_list
    else:
        context['response'] = "API Key not registered!"
        context['data'] = []

    return JsonResponse(context, safe=False)