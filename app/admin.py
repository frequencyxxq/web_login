from django.contrib import admin

# Register your models here.
from .models import Ticket, Organization, Room, IssueCategory, IssueSubcategory


class CustomModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields if field.name != "id"
        ]
        super(CustomModelAdmin, self).__init__(model, admin_site)


class TicketAdmin(CustomModelAdmin):
    list_filter = [
        "user__username",
        "created_at",
        "reporter",
        "solved_by",
        "mobile_phone",
    ]
    search_fields = ["user__username", "mobile_phone", "reporter", "solved_by"]


class OrganizationAdmin(CustomModelAdmin):
    pass


class RoomAdmin(CustomModelAdmin):
    pass


class IssueCategoryAdmin(CustomModelAdmin):
    pass


class IssueSubcategoryAdmin(CustomModelAdmin):
    pass


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(IssueCategory, IssueCategoryAdmin)
admin.site.register(IssueSubcategory, IssueSubcategoryAdmin)
