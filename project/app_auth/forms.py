from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "first_name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "last_name": forms.TextInput(attrs={"class": "form-control form-control-lg"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control form-control-lg"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control form-control-lg"}),
        }

# <div class="row mb-3">
#         <div class="col">
#           <label class="col-sm-4 col-form-label offset-4">Name</label>
#           <div class="col-sm-4 offset-4 w-25">
#             <input type="text" class="form-control form-control-lg">
#           </div>
#         </div>
#       </div>
#       <div class="row mb-3">
#         <div class="col">
#           <label class="col-sm-4 col-form-label offset-4">Surname</label>
#           <div class="col-sm-4 offset-4 w-25">
#             <input type="text" class="form-control form-control-lg">
#           </div>
#         </div>
#       </div>
#       <div class="row mb-3">
#         <div class="col">
#           <label class="col-sm-4 col-form-label offset-4">Password</label>
#           <div class="col-sm-4 offset-4 w-25">
#             <input type="password" class="form-control form-control-lg">
#           </div>
#         </div>
#       </div>
#       <div class="row mb-3">
#         <div class="col">
#           <label class="col-sm-4 col-form-label offset-4">Password confirmation</label>
#           <div class="col-sm-4 offset-4 w-25">
#             <input type="password" class="form-control form-control-lg">
#             <div class="form-label bg-warning" style="margin: 10px 0px;">Ошибка (если будет)</div>
#           </div>
#         </div>
#       </div>
