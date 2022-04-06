from datetime import datetime
from pickletools import read_uint1
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from mirai.models import Company,Employee, Task
from mirai.forms import CompanyForm, EmployeeForm, loginForm, TaskForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.db.models import Q
from django.db.models.functions import Concat
from .models import Employee
from .resources import EmployeeResource
from tablib import Dataset
# Create your views here.
from django.views.generic import  ListView


class SearchResultsView(ListView):
    model = Employee
    template_name = 'search.html'
    print("hello")
    def get_queryset(self): # new

        query = self.request.GET.get("q")
        print(query)
        object_list= Employee.objects.filter(
            Q(empcode__icontains=query)         )
        object_list=Employee.objects.filter( Q(eFname__icontains=query) | Q(eLname__icontains=query) | Q(eEmail__icontains=query) | Q(ePhone__icontains=query) | Q(eCompany__icontains=query))
    
        print(object_list)
        return object_list



def loginCheck(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = "admin", password = "adminl12345")
        if user is not None:
            auth.login(request, user)
            return redirect("/emp")
        else:
            messages.info(request, 'invalid credentials')
            return redirect



    else:
        form = loginForm()
        return render(request, "regsitration/login.html")


def simple_upload(request):
    if request.method == 'POST':
        person_resource = EmployeeResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            value = Employee(data[0],data[1],data[2],data[3],data[4],data[5])
            value.save()  
    
    return redirect("/showemp")

#Home page
def home(request):
    return redirect(request,"")


def export(request):
    person_resource = EmployeeResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response
# To create Company
def comp(request):
    if request.method == "POST":

        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})

# To retrieve Company details
def show(request):
    companies = Company.objects.all()
    return render(request, "show.html", {'companies':companies})

# To Edit Company details
def edit(request, cName):
    company = Company.objects.get(cName=cName)
    return render(request, "edit.html", {'company':company})

# To Update Company
def update(request, cName):
    company = Company.objects.get(cName=cName)
    form = CompanyForm(request.POST, instance= company)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'company': company})

# To Delete Company details
def delete(request, cName):
    company = Company.objects.get(cName=cName)
    company.delete()
    return redirect("/show")


# To create employee
def emp(request):
    if request.method == "POST":

        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, eFname):
    employee = Employee.objects.get(eFname=eFname)
    form=EmployeeForm(request.POST, instance= employee)
    if form.is_valid():
        form.save()
        return redirect("/show")    
    return render(request, "editemployee.html", {'employee':employee})

# To update employee details
def updateEmp(request, pk):
    employee = Employee.objects.get(empcode=pk)
    form = EmployeeForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid():
        
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})


# def filter_emp(request, eFname):
#     if request.method=='POST':
#         name = request.POST['Fname']
#         print(name)
#         fname = Employee.objects.get(eFname=eFname)
#         print(fname)
#         # c_name = request.POST['eCompany']
#         employee=Employee.objects.all()
#         if name:
#             emps=Employee.objects.filter(fname==name)
#         context={
#             'emps':emps
#         }


#         return render(request,"showemp.html",context)

#     elif request.method =='GET':
#         return render(request,'filter_emp.html')
#     else:
#         return HttpResponse('An exception occured')


# def search(request):
#     if request.method == 'GET':
#         query= request.GET.get('q')

#         submitbutton= request.GET.get('submit')

#         if query is not None:
#             lookups= Q(eFname__icontains=query) | Q(eLname__icontains=query)

#             results= Employee.objects.filter(lookups).distinct()

#             context={'results': results,
#                      'submitbutton': submitbutton}

#             return render(request, 'showemp.html', context)

#         else:
#             return render(request, 'showemp.html')

#     else:
#         return render(request, 'showemp.html')
# def search(request):
#     if request.method == 'POST':      
#         search =  request.POST.getlist('search')      
#         try:
#             status = Employee.objects.filter(eFname__icontains=search)
#             #Add_prod class contains a column called 'bookname'
#         except Employee.DoesNotExist:
#             status = None
#         return render(request,"search.html",{"books":status})
#     else:
#         return render(request,"search.html",{})













def task(request):
    if request.method == "POST":

        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                
                form.save()
                return redirect("showtask")
            except:
                pass
    else:
        form = TaskForm()
    return render(request, "addtask.html", {'form':form})

def showtask(request):
    task = Task.objects.all()
    print(task)
    return render(request, "showtask.html", {'task':task})

def add_task(request, eFname):
    tasksemp = Employee.objects.filter(eFname==eFname)
    print(tasksemp)
    task = get_object_or_404(Task, task_user=tasksemp)
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save_user(request)
        else:
            print("form not valid")
            print(form.errors)
            print(request.POST.get('task_goal'))
    return redirect('task')             # Finally, redirect to the homepage.




def add_goal(request):
    print("friens")
    # tasksemp = Employee.objects.filter(eFname==eFname)
    print("hello")
    # task = get_object_or_404(Goal, goal_sett=eFname)
    if request.method == 'GET':
        # Create a form instance and populate it with data from the request (binding):
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('task/')         