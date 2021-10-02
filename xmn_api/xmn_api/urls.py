
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Register/',include('Register.urls')),
    # path('Student_Data/',include('Student_Data.urls')),
    # path('Messages/',include('Messages.urls')),
    # path('Curriculum/',include('Curriculum.urls')),
    # path('System/',include('System.urls')),
]
