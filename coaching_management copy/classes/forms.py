
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2', 'is_student', 'is_admin')
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password1'].help_text = None
#         self.fields['password2'].help_text = None

# class CustomUserAuthenticationForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')

# from django import forms
# from .models import Course

# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['name', 'description', 'fees', 'faculty_name', 'duration']  # Updated fields

        


# NEW

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Course

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_student', 'is_admin')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'fees', 'faculty_name', 'duration']
