from django.urls import path
from modules.experiments.views import module_crud
from modules.experiments.views import module_crud_id

urlpatterns = [
    path('', module_crud),   
    path('<int:id>', module_crud_id),   
]