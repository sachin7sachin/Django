from django.urls import path
from . import views

urlpatterns = [
    path("",views.all_chai,name = "all_chai"),
    path("<int:id>/",views.chai_details,name = "chai_details"),
    path("chai_store/",views.chai_store_view, name = "chai_store")
]