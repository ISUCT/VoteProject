# coding: utf8
from forms import AdminUserChangeForm, AdminUserAddForm
from forms import AdminStudentAddForm, AdminStudentChangeForm
from models import Stuff, Student
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

# Указываем наши форма для создания и редактирования пользователя.
# Добавляем новые поля в fieldsets, и поле email в add_fieldsets.
class UserAdmin(BaseUserAdmin):
    form = AdminUserChangeForm
    add_form = AdminUserAddForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}), # Вот тут я не знаю что и как...
        (_('Personal info'), {'fields': (
            'surname', # Передаем наши поля
            'name',
            'patronymic',
            'login',
            'chair'
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),

            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )



class StudentAdmin(BaseUserAdmin):
    form = AdminStudentChangeForm
    add_form = AdminStudentAddForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}), # Вот тут я не знаю что и как...
        (_('Personal info'), {'fields': (
            'login', # Передаем наши поля
            'surname',
            'name',
            'patronymic',
            'group'
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),

            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

admin.site.register(Stuff, UserAdmin)
admin.site.register(Student, StudentAdmin)
