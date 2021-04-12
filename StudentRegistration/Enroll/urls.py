from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Add_show,name='Add_show_page'),
    path('Delete/<int:id>/',views.Delete,name='Delete_page'),
    path('Update/<int:id>/',views.Update,name='Update_page')
]