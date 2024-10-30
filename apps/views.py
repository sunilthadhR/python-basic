from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import User,Usermobile,Employee,Payroll,LeaveApplication,CompensativeLeaveApplication,Refer_friends
import hashlib
from django.contrib import messages


VALID_ADMIN_ID = "admin123"  

def admin_check(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        if admin_id == VALID_ADMIN_ID:
            return redirect('employee_signup') 
        else:
            return render(request, 'admin.html', {
                'error_message': 'Invalid Admin ID. Please try again.'
            })
    
    return render(request, 'admin.html',context={'value':'Admin'})

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,'contact.html')

def check_password(password,user):
        password = hashlib.sha256(password.encode()).hexdigest()
        if password == user:
            return True
        else:
            return False

def employee_signup(request):
    if request.method == 'POST':
        user = User.objects.filter(phone_number=request.POST.get('phone_number', '')).last()
        if user:
            messages.error(request, "user already register.")
            context={"message":"Employee already register "}
            return render(request, 'pop.html', context=context)
        if not user:
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            role=request.POST['role']
            phone_number = request.POST.get('phone_number', '')
            address = request.POST.get('address', '')
            date_of_birth = request.POST.get('date_of_birth', '')

            employee_id= request.POST.get('employee_id', '')
            department=request.POST.get('department', '')
            designation=request.POST.get('designation', '')
            date_of_joining=request.POST.get('date_of_joining', '')
            salary=request.POST.get('salary', '')

            pay_date=request.POST.get('pay_date', '')
            basic_salary=request.POST.get('basic_salary', '')
            pf=request.POST.get('pf', '')
            deductions=request.POST.get('deductions', '')
            net_pay=request.POST.get('net_pay', '')

            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                role=role,
                password=hashlib.sha256(password.encode()).hexdigest(),
                phone_number=phone_number,
                address=address,
                date_of_birth=date_of_birth,
                is_staff=True if role == 'admin' else False
            )
            emp=Employee.objects.create(
                user=user,
                employee_id=employee_id,
                department=department,
                designation=designation,
                date_of_joining=date_of_joining,
                salary=salary
            )
            pay=Payroll.objects.create(
                employee=emp,
                pay_date=pay_date,
                basic_salary=basic_salary,
                pf=pf,
                deductions=deductions,
                net_pay=net_pay
            )
            messages.success(request, 'Employee registered successfully.')
            Usermobile.objects.create(user=user,mobile_no=user.phone_number)
            return redirect('home')
    
    return render(request, 'employee_signup.html')




def employee_login(request):
    if request.method == 'POST':
        password = request.POST['password']
        mobile_no = request.POST.get('login_id', '')
        try:
            user_mobile = Usermobile.objects.filter(mobile_no=mobile_no).last()
            if not user_mobile:
                context = {'message': 'Invalid phone number'}
                return render(request, 'pop.html', context=context)
            if user_mobile and not check_password(password, user_mobile.user.password):
                context = {'message': 'Invalid password'}
                return render(request, 'pop.html', context=context)

            if user_mobile and check_password(password, user_mobile.user.password):
                    mobile_update=Usermobile.objects.filter(mobile_no=mobile_no).last()
                    mobile_update.user_status=1
                    mobile_update.save()

                    request.session['mobile_no'] = mobile_no
                    request.session.save()

                    return redirect('employee_homepage')
            else:
                context = {'message': 'Invalid phone number and password'}
                return render(request, 'pop.html', context=context)    
        except Exception as e:
            context = {'error': 'An error occurred: {}'.format(str(e))}
            return render(request, 'pop.html', context=context)
    
    return render(request, 'employee_login.html')


def employee_logout(request):
    try:
        mobile_no = request.session.get('mobile_no')
        if mobile_no:
            user_mobile = Usermobile.objects.filter(mobile_no=mobile_no).last()
            if user_mobile:
                user_mobile.user_status = 0
                user_mobile.save()
            return redirect('home')
        request.session.flush()
        return redirect('employee_login')
    except Exception as e:
        context = {'error': 'An error occurred during logout: {}'.format(str(e))}
        return render(request, 'pop.html', context=context)

def forget_password(request):
    if request.method == 'POST':
        login_id = request.POST.get('login_id','')
        try:
            user=User.objects.filter(phone_number=login_id).last()
            if user:
                context = {"login_id": login_id}
                return render(request, 'change_password.html', context=context)
            else:
                context={"message":"Invaid Mobile number"}
                return render(request, 'pop.html', context=context)
        except Exception as e:
            return e
    return render(request, 'forget_password.html')

def change_pass(request):
    if request.method == 'POST':
        login_id = request.POST.get('login_id', '')
        change_password = request.POST.get('change_password','')
        confirm_password = request.POST.get('confirm_password','')
        if change_password==confirm_password:
            if login_id:
                user_update=User.objects.filter(phone_number=login_id).last()
                if user_update:
                    user_update.password=hashlib.sha256(confirm_password.encode()).hexdigest()
                    user_update.save()
            context={"success":"Successfully updated your password, Kindly login now"}
            return render(request, 'pop.html', context=context)
        else:
            context={"error":"New password and Confirm password do not match."}
            return render(request, 'pop.html', context=context)
    return render(request, 'change_password.html')

def employee_homepage(request):
    mobile_no = request.session.get('mobile_no')
    user_no = User.objects.filter(phone_number=mobile_no).last()
    emp_number = Employee.objects.filter(user_id=user_no.id).last()
    context = {}
    if emp_number:
        context["employee_id"] = emp_number.employee_id
        context["phone"] = user_no.phone_number
        context["employee_name"] = user_no.first_name
        context["designation"] = emp_number.designation
    return render(request, 'employee_homepage.html', context)


def attendance(request):
    mobile_no = request.session.get('mobile_no')
    user_no = User.objects.filter(phone_number=mobile_no).last()
    emp_number = Employee.objects.filter(user_id=user_no.id).last()
    context = {}
    context = {'value':'Attendance'}
    context["employee_name"] = user_no.first_name
    context["designation"] = emp_number.designation
    context["days_present"] = 20
    context["days_absent"] = 4
    return render(request, 'attendance.html', context=context)

def payslip(request):
    mobile_no = request.session.get('mobile_no')
    user_no = User.objects.filter(phone_number=mobile_no).last()
    emp_number = Employee.objects.filter(user_id=user_no.id).last()
    pay_roll = Payroll.objects.filter(employee=emp_number.id).last()
    context={}
    context['value'] = "Payslip Details"
    if pay_roll:
        context["pay_period"] = pay_roll.pay_date
        context["basic_salary"] = pay_roll.basic_salary
        context["hra"] = 1000
        context["tax"] = pay_roll.deductions
        context['pf'] = pay_roll.pf
        context["other_allowances"] = 0
        context["net_salary"] = pay_roll.net_pay+1000
    if emp_number:
        context["employee_name"] = user_no.first_name
        context["designation"] = emp_number.designation

    return render(request,'payslip.html',context=context)

def apply_leave(request):
    mobile_no = request.session.get('mobile_no')
    user_no = User.objects.filter(phone_number=mobile_no).last()
    emp_number = Employee.objects.filter(user_id=user_no.id).last()
    context = {}
    context = {'value':'Apply_Leave'}
    context["employee_name"] = user_no.first_name
    context["designation"] = emp_number.designation
    if request.method == 'POST':
        mobile_no = request.session.get('mobile_no')
        leave_type = request.POST['leave_type']
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        reason = request.POST.get('reason', '')
        if mobile_no:
            user_id = User.objects.filter(phone_number=mobile_no).last()
            create_date=LeaveApplication.objects.create(
                user=user_id,
                leave_type=leave_type,
                start_date=start_date,
                end_date=end_date,
                reason=reason
                )
            context={"ApplySuccess":"Successfully applied your leave"}
            return render(request, 'pop.html', context=context)
        else:
            context={"error":"kindly login and apply your leaves"}
            return render(request, 'pop.html', context=context)
    return render(request,'apply_leave.html',context=context)

def compensative_apply(request):
    mobile_no = request.session.get('mobile_no')
    user_no = User.objects.filter(phone_number=mobile_no).last()
    emp_number = Employee.objects.filter(user_id=user_no.id).last()
    context = {}
    context = {'value':'Compensative_apply'}
    context["employee_name"] = user_no.first_name
    context["designation"] = emp_number.designation
    if request.method == 'POST':
        mobile_no = request.session.get('mobile_no')
        work_date = request.POST.get('work_date','')
        compensative_date = request.POST.get('compensative_date', '')
        reason = request.POST.get('reason', '')
        if mobile_no:
            user_id = User.objects.filter(phone_number=mobile_no).last()
            create_date=CompensativeLeaveApplication.objects.create(
                user=user_id,
                work_date=work_date,
                compensative_date=compensative_date,
                reason=reason
                )
            context={"ApplySuccess":"Successfully applied your compensative leave"}
            return render(request, 'pop.html', context=context)
        else:
            context={"error":"kindly login and apply your leaves"}
            return render(request, 'pop.html', context=context)
    return render(request,'compensative_apply.html',context=context)

def Refer_Friend(request):
    mobile_no = request.session.get('mobile_no')
    user_no=User.objects.filter(phone_number=mobile_no).last()
    emp_number=Employee.objects.filter(user_id=user_no.id).last()
    context={}
    context={'value':'Refer_Friend'}
    context["employee_name"] = user_no.first_name
    context["designation"] = emp_number.designation
    if request.method == 'POST':
        mobile_no = request.session.get('mobile_no')
        your_name = request.POST.get('your_name','')
        friend_name = request.POST.get('friend_name', '')
        friend_mobile = request.POST.get('friend_mobile', '')
        message = request.POST.get('message', '')
        
        if mobile_no:

            user_id = User.objects.filter(phone_number=mobile_no).last()
            create_date=Refer_friends.objects.create(
                user=user_id,
                your_name=your_name,
                friend_name=friend_name,
                friend_mobile=friend_mobile,
                message=message
                )
            
            context={"ApplySuccess":"Successfully applied your Refer"}
            return render(request, 'pop.html', context=context)
        
        else:
            context={"error":"kindly login and apply."}
            return render(request, 'pop.html', context=context)
        
    return render(request,'Refer_Friend.html',context=context)

def event(request):
    mobile_no = request.session.get('mobile_no')
    user_no = User.objects.filter(phone_number=mobile_no).last()
    emp_number = Employee.objects.filter(user_id=user_no.id).last()
    context = {}
    context = {'value':'Event'}
    context["employee_name"] = user_no.first_name
    context["designation"] = emp_number.designation
    return render(request,'event.html',context=context)




















































































































































