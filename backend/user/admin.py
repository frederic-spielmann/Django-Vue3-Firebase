from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from firebase_admin import auth as firebase_auth
from django.db import IntegrityError

from .models import FirebaseUser


def firebase_create_user(obj):
    """
    Function to create a new user from Firebase app
    1) on creating a new user from admin panel (or)
    2) to create firebase user for existing users in django db
    """
    try:
        data = {"uid": str(obj.uid)}
        if obj.email:
            data.update({"email": obj.email})
        firebase_auth.create_user(**data)
    except firebase_auth.UidAlreadyExistsError:
        raise IntegrityError("Uid already exists")


def create_firebaseuser_from_admin(FirebaseUserModel, request, queryset):
    """
    To create a user in firebase corresponding to selected existing user in Admin panel
    """
    for obj in queryset:
        firebase_create_user(obj)


def delete_firebase_user(obj):
    """
    To delete a user from firebase on deleting it from our database
    """
    try:
        print("Deleting uid from firebase - ", obj.uid)
        firebase_auth.delete_user(obj.uid)
    except:
        pass


# Action description to display in Admin Panel actions
create_firebaseuser_from_admin.short_description = (
    "Create Firebase users from selected users"
)


@admin.register(FirebaseUser)
class FirebaseUserAdmin(BaseUserAdmin):
    """
    Admin view for FirebaseUser
    """

    list_display = (
        "identifier",
        "email",
    )
    list_filter = ("is_staff", "is_superuser",
                               "is_active", "groups", "date_joined")
    fieldsets = (
        (
            None,
            {
                "fields": ("uid", "password"),
            },
        ),
        (
            "Personal info",
            {
                "fields": ("display_name", "email"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    ("is_active", "is_staff", "is_superuser"),
                    ("groups", "user_permissions"),
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": ("last_login", "date_joined"),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    search_fields = ("uid", "display_name", "email")

    ordering = (
        "-date_joined",
        "display_name",
    )

    actions = [create_firebaseuser_from_admin]

    def save_model(self, request, obj, form, change):
        if not obj.id:
            """
            To create a user in firebase upon creating a new user from admin
            """
            firebase_create_user(obj)
        elif change:
            """
            To update an existing user in firebase, to add/change email
            when change from admin panel
            """
            try:
                firebase_auth.get_user(obj.uid)
                data = {}
                if "email" in form.changed_data:
                    data.update({"email": obj.email})
                if data:
                    updated = firebase_auth.update_user(obj.uid, **data)
            except:
                pass
        super().save_model(request, obj, form, change)

    def delete_queryset(self, request, queryset):
        """
        To delete firebase users on deleting users from admin panel - bulk delete action
        """
        dict_uids = queryset.values("uid")
        uids = [item["uid"] for item in dict_uids]
        try:
            firebase_auth.delete_users(uids)
        except:
            pass
        queryset.delete()

    def delete_model(self, request, obj):
        """
        To delete firebase user on deleting a single user from admin panel - object level deletion
        """
        delete_firebase_user(obj)
        obj.delete()
