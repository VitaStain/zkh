from django.urls import include, path

from apps.orders.views.order import OrderCreateView

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("orders/", OrderCreateView.as_view()),
            ]
        ),
    ),
]
