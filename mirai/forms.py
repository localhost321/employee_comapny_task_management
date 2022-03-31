from django import forms
from mirai.models import Employee, Login, Task
from mirai.models import Company

# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

#this is for company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class loginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = "__all__"


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    # def save_user(self, request):
    #     obj = self.save(commit=False)
    #     obj.task_user = request.user
    #     obj.save()
        # self.save()

        

# class GoalForm(forms.ModelForm):
#     class Meta:
#         model = Goal
#         fields = '__all__'

