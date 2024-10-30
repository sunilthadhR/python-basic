from django.contrib import admin
from .models import Employee,User,Usermobile,Payroll,LeaveApplication,CompensativeLeaveApplication,Refer_friends


# Register your models here.

admin.site.register(User)
admin.site.register(Usermobile)
admin.site.register(Employee)
admin.site.register(Payroll)
admin.site.register(LeaveApplication)
admin.site.register(CompensativeLeaveApplication)
admin.site.register(Refer_friends)