from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.accounts.views.customer import CustomerListView
from apps.accounts.views.registration import AccountProfileCreateView

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path(
                    "api/token/",
                    TokenObtainPairView.as_view(),
                    name="token_obtain_pair",
                ),
                path(
                    "api/token/refresh/",
                    TokenRefreshView.as_view(),
                    name="token_refresh",
                ),
                path(
                    "registration/",
                    AccountProfileCreateView.as_view(),
                    name="registration",
                ),
                path(
                    "customers/",
                    CustomerListView.as_view(),
                ),
            ]
        ),
    ),
]
