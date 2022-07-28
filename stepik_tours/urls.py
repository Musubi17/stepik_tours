from django.contrib import admin
from django.urls import path

from tours.views import main_view
from tours.views import departure_view
from tours.views import tour_view


urlpatterns = [
    path('', main_view, name='main'),
    path('departure/<str:departure>/', departure_view),
    path('tour/<int:tour_id>/', tour_view),
    path('admin/', admin.site.urls),
]
