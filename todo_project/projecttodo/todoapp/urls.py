from .import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
     path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    path('cdvhome/', views.Listview.as_view(), name="cdvhome"),
    path('detail/<int:pk>/', views.Detailview.as_view(), name="cdvdetail"),
    path('update/<int:pk>/', views.Updateview.as_view(), name="cdvupdate"),
    path('delete/<int:pk>/', views.Detailview.as_view(), name="cdvdelete"),
]