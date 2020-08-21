from django.urls import path
from modules.devices.views import module_crud
from modules.devices.views import module_crud_id
from modules.devices.views import send_command_to_device

urlpatterns = [
    path('', module_crud),   
    path('<int:id>', module_crud_id),   
    path('send/uid/<int:uid>/command/<str:command>', send_command_to_device), 
]