from django.urls import path
from . import views

urlpatterns = [
    path('pdf/', views.generate_PDF_from_selected_section, name="pdf"),
    path('', views.page, name="page"),
]
