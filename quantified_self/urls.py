from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/foods/(?P<pk>[0-9]+)$',
        views.get_delete_update_food,
        name='get_delete_update_food'
    ),
    url(
        r'^api/v1/foods/$',
        views.get_post_food,
        name='get_post_food'
    ),
]
