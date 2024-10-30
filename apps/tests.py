from django.test import TestCase

# Create your tests here.

import hashlib
import base64


# <!-- <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Employee Login</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             margin: 30;
#             padding: 30;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             height: 50vh;
#         }
#         .login-container {
#             background-color: #ffffff;
#             padding: 50px;
#             border-radius: 10px;
#             box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
#             width: 400px;
#         }
#         .login-container h2 {
#             text-align: center;
#             margin-bottom: 50px;
#         }
#         .login-container label {
#             display: block;
#             margin-bottom: 20px;
#             font-weight: bold;
#         }
#         .login-container input[type="text"],
#         .login-container input[type="password"] {
#             width: 100%;
#             padding: 10px;
#             margin-bottom: 20px;
#             border: 1px solid #ccc;
#             border-radius: 4px;
#             box-sizing: border-box;
#         }
#         .login-container input[type="submit"] {
#             background-color: #4CAF50;
#             color: white;
#             padding: 10px;
#             border: none;
#             border-radius: 4px;
#             cursor: pointer;
#             width: 100%;
#         }
#         .login-container input[type="submit"]:hover {
#             background-color: #45a049;
#         }
#     </style>
# </head>
# <body>
#     <div class="login-container">
#         <h2>Employee Login</h2>
#         <form action="{% url 'employee_login' %}" method="post">
#             {% csrf_token %}
#             <label for="phone_number">Phone Number:</label>
#             <input type="text" id="phone_number" name="phone_number" required>

#             <label for="password">Password:</label>
#             <input type="password" id="password" name="password" required>

#             <input type="submit" value="Login">
#         </form>
#     </div>

# </body>
# </html> -->
# def check_password(password,user):
#         password = hashlib.sha256(password.encode()).hexdigest()
#         if password == user:
#             return True
#         else:
#             return False
        
# password="gokul"

# # print(p)

# password='7619414836'
# # l1=base64.b64encode(mobile_obj.mobile.encode('utf-8'))
# p = hashlib.sha256(password.encode()).hexdigest()
# print(p)


# m="7619414836"
# l1=base64.b64encode(m.encode('utf-8'))
# print(l1)

# def employee_login(request):
#     if request.method == 'POST':
#         password = request.POST['password']
#         phone_number=request.POST.get('phone_number', '')
#         try:
#             user=User.objects.filter(phone_number=phone_number).last()
#             if not user:
#                 context={'message':'Invalid phone number'}
#                 return render(request, 'pop.html',context=context)
#             mobile_user=Usermobile.objects.filter(mobile_no=phone_number).last()
#             if mobile_user:
#                 password=check_password(password,user.password)
#                 if mobile_user and password:
#                     return redirect('employee_homepage') 
#                 else:
#                    context={'error': 'Invalid password'}
#                    return render(request, 'pop.html', context=context)
#             else:
#                 return redirect('employee_signup')
#         except Exception as e:
#             return e
#     return render(request, 'employee_login.html')

# import random
# import string
# l1=string.digits
# # print(type(l1))
# result = ''.join((random.choice(l1)) for x in range(4))
# print(result)




























