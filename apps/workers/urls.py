from django.urls import include, path

from apps.workers.views.worker import WorkerListCreateView, WorkerDetailUpdateDeleteView

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("admin/workers/", WorkerListCreateView.as_view()),
                path("admin/workers/<int:pk>/", WorkerDetailUpdateDeleteView.as_view()),
            ]
        ),
    ),
]
