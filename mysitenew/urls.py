from django.contrib import admin
from django.urls import path
from newapp.views import *

urlpatterns = [
    path('admin-old/', admin.site.urls),
    path('admin/', admin_login_page),
    path('admin-page/', admin_page),
    path('', main_page),
    path('form-page/<int:lang>', form_page),
    path('success/<int:lang>', success_page),

    path('api/v1/get-all-data/<str:key>', api_call)
]
