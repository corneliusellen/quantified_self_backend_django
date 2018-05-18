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
    url(
        r'^api/v1/meals',
        views.get_meals,
        name='get_meals'
    ),
    url(
        r'^api/v1/meals/(?P<pk>[0-9]+)/foods',
        views.get_meal_foods,
        name='get_meal_foods'
    ),
]
