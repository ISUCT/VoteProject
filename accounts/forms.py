# coding: utf8
from models import Stuff, Student
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Допиливаем форму добавления пользователя. В Meta.model указываем нашу модель.
# Поля указывать нет необходимости т.к. они переопределяются в UserAdmin.add_fieldsets
class AdminUserAddForm(UserCreationForm):

    class Meta:
        model = Stuff

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Stuff._default_manager.get(username=username)
        except Stuff.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

# Допиливаем форму редактирования пользователя. В Meta.model указываем нашу модель.
class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = Stuff

# Делаем то же самое для студента

class AdminStudentAddForm(UserCreationForm):
    class Meta:
        model = Student
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Student._default_manager.get(username=username)
        except Student.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class AdminStudentChangeForm(UserChangeForm):
    class Meta:
        model = Student



