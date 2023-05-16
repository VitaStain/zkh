from django.urls import include, path

from apps.services.views.service import (
    ServiceCreateView,
    ServiceDetailPatchDeleteView,
    ServiceListView,
)

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("admin/services/", ServiceCreateView.as_view()),
                path(
                    "admin/services/<int:pk>/", ServiceDetailPatchDeleteView.as_view()
                ),
                path("services/", ServiceListView.as_view()),
            ]
        ),
    ),
]
