from django.contrib import admin

# Register your models here.
# admin 페이지는 장고 기본 User 모델에 종속되어 있으므로 User 인스턴스에  Profile 인스턴스가 포함되어 있는 형태로 보기 위한 코드
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)