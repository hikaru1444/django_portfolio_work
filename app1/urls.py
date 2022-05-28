from django.urls import path
from app1.views import top, work
urlpatterns = [
    path('top/', top, name='top'),
    path('work/', work, name='work'),
]