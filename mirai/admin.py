from concurrent.futures.process import _threads_wakeups
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from mirai.models import Company, Employee, Login, Task

# Register your models here.
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Login)
admin.site.register(Task)
# admin.site.register(Day)
# admin.site.register(Goal)
class EmployeeAdmin(ImportExportModelAdmin):
    list_display=('eFname','eLname','eCompany','eEmail','ePhone')
