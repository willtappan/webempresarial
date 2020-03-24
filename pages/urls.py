from django.urls import path
from . import views
urlpatterns = [ 
    path('<int:page_id>/', views.page, name="page"), #le paa un parametro /<category_id>/ string
]

