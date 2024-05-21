from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CustomUser, Course, Registration
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CourseForm

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'classes/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'classes/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.is_admin:
        courses = Course.objects.all()
        registrations = Registration.objects.all()
        context = {
            'courses': courses,
            'registrations': registrations
        }
        return render(request, 'classes/admin_dashboard.html', context)
    elif request.user.is_student:
        courses = Course.objects.all()
        registered_courses = Registration.objects.filter(student=request.user).values_list('course', flat=True)
        registrations = Registration.objects.filter(student=request.user)
        context = {
            'courses': courses,
            'registered_courses': registered_courses,
            'registrations': registrations
        }
        return render(request, 'classes/student_dashboard.html', context)
    else:
        return redirect('login')

@login_required
@user_passes_test(lambda u: u.is_admin)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CourseForm()
    return render(request, 'classes/add_course.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_admin)
def view_registrations(request):
    registrations = Registration.objects.all()
    return render(request, 'classes/view_registrations.html', {'registrations': registrations})

@login_required
def register_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    registration, created = Registration.objects.get_or_create(student=request.user, course=course)
    return redirect('dashboard')

@login_required
@user_passes_test(lambda u: u.is_admin)
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('dashboard')
