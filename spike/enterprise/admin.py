from django.contrib import admin
from enterprise.models import Enterprise

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_filter=("name",)
    list_display=(
        "name",
        "email",
        "phone",
        "active",
    )
    fieldsets=(
        "Datos de la empresa",
        {
            "fields":(
                "name",
                "email",
                "phone",
                "active"
            )

        },
    ),