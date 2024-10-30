from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('hr', 'HR Personnel'),
        ('employee', 'Employee'),
    ]
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_staff=models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
  
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pay_date = models.DateField()
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    pf = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

class Usermobile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_status=models.IntegerField(default=0)
    mobile_no = models.CharField(max_length=10,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class LeaveApplication(models.Model):
    LEAVE_TYPE_CHOICES = [
    ('sick', 'Sick Leave'),
    ('casual', 'Casual Leave'),
    ('earned', 'Earned Leave'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()


class CompensativeLeaveApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    work_date = models.DateField() 
    compensative_date = models.DateField()  
    reason = models.TextField()


class Refer_friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    your_name = models.CharField(max_length=100)
    friend_name = models.CharField(max_length=100)
    friend_mobile = models.CharField(max_length=10) 
    message = models.TextField(blank=True) 