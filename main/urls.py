from django.urls import path

from main.apps import MainConfig
from main.views import home_page, MassageListView, MassageCreateView, MassageDetailView, MassageDeleteView, \
    MassageUpdateView

app_name = MainConfig.name

urlpatterns = [
    path('', home_page, name='home'),
    path('messenger/', MassageListView.as_view(), name='messenger_list'),
    path('messenger/create', MassageCreateView.as_view(), name='messenger_create'),
    path('messenger/<int:pk>', MassageDetailView.as_view(), name='messenger_view'),
    path('messenger/delete/<int:pk>', MassageDeleteView.as_view(), name='messenger_delete'),
    path('messenger/edit/<int:pk>', MassageUpdateView.as_view(), name='messenger_update')
]
