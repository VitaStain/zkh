from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from apps.accounts.models.account import Account

admin.AdminSite.site_header = _("Администрирование PAINT")


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ("pk", "email", "created_at", "is_active", "is_staff")
    list_display_links = ("pk", "email")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "created_at",
                    "updated_at",
                    "deleted_at",
                    "password",
                )
            },
        ),
        (
            # _("Permissions"),
            "Разрешения",
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("password1", "password2")
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
