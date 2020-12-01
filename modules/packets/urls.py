from django.urls import path
from modules.packets.views import module_crud
from modules.packets.views import module_crud_id
from modules.packets.views import method_get_device_id_exp_id
from modules.packets.views import handle_tcp_packet
from modules.packets.views import get_ch4_packets_by_experiment_id
from modules.packets.views import delete_packets_by_experiment_id

urlpatterns = [
    path('', module_crud),   
    #path('<int:id>', module_crud_id),   
    path('device/<int:device_id>/experiment/<int:experiment_id>', method_get_device_id_exp_id),   
    path('by/experimentId/<int:experiment_id>', get_ch4_packets_by_experiment_id),   
    path('delete/by/experimentId/<int:experiment_id>', delete_packets_by_experiment_id),
    path('handle_tcp_packet', handle_tcp_packet) 
    
]


