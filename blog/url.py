from django.urls import path
from .views import *
from .machine.hardware import pc

urlpatterns = [
    path('cip/', client_ip),
    path('sip', server_ip),
    path('pc/', pc),
    path('files/<str:filename>', FileUploadView.as_view()),
]