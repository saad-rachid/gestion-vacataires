from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
#admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['cin','name','email','date_created','admin']
    list_filter = ['admin', 'groups']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('cin','name')}),
        ('Permissions', {'fields': ('is_active','staff','admin', 'groups')}),
        ('Important dates', {'fields': ('last_login',)}),
    )


    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cin', 'name','email','groups','password', 'password_2')
            }
        ),
    )
    search_fields = ['cin']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
