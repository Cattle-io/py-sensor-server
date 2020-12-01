from django.urls import path
from modules.experiments.views import module_crud
from modules.experiments.views import module_crud_id
from modules.experiments.views import do_play_by_id
from modules.experiments.views import do_pause_by_id

urlpatterns = [
    path('', module_crud),   
    path('<int:id>', module_crud_id),   
    path('do/play/by/id/<int:experiment_id>', do_play_by_id),   
    path('do/pause/by/id/<int:experiment_id>', do_pause_by_id)   
]