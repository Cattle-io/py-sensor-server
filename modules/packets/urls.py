from django.urls import path
from modules.packets.views import module_crud
from modules.packets.views import module_crud_id
from modules.packets.views import method_get_device_id_exp_id

urlpatterns = [
    path('', module_crud),   
    #path('<int:id>', module_crud_id),   
    path('device/<int:device_id>/experiment/<int:experiment_id>', method_get_device_id_exp_id),   
]