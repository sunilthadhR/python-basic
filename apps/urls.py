from django.urls import path
from apps.views import home, employee_signup, employee_login , employee_logout,employee_homepage,attendance,forget_password,admin_check,contact,change_pass,\
    payslip,apply_leave,compensative_apply,Refer_Friend,event
                         

urlpatterns = [
    path('', home, name='home'),
    path('employee_signup/',employee_signup, name='employee_signup'),
    path('employee_login/',employee_login, name='employee_login'),
    path('employee_logout/',employee_logout,name='employee_logout'),
    path('employee_homepage/',employee_homepage,name="employee_homepage"),
    path('attendance/', attendance, name='attendance'),
    path('forget_password/',forget_password,name='forget_password'),
    path('admin_check/',admin_check,name='admin_check'),
    path('contact/',contact,name='contact'),
    path('change_pass/',change_pass,name='change_pass'),
    path('payslip/',payslip ,name='payslip'),
    path('apply_leave/',apply_leave,name='apply_leave'),
    path('compensative_apply/',compensative_apply,name='compensative_apply'),
    path('Refer_Friend/',Refer_Friend,name='Refer_Friend'),
    path('event/',event,name='event')
]