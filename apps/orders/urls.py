from django.urls import include, path

from apps.orders.views.order import (
    OrderCreateView,
    OrderListView,
    OrderDetailView,
    OrderUpdateView,
)

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("orders/", OrderCreateView.as_view()),
                path("admin/orders/", OrderListView.as_view()),
                path("admin/orders/<int:pk>/", OrderDetailView.as_view()),
                path("admin/orders/<int:pk>/worker/", OrderUpdateView.as_view()),
            ]
        ),
    ),
]
