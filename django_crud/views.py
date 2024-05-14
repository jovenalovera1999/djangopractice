from django.shortcuts import render, redirect
from .models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.

def gender_index(request):
    genders = Gender.objects.all()

    context = {
        'genders': genders
    }

    return render(request, 'gender/index.html', context)

def gender_show(request, id):
    gender = Gender.objects.get(pk=id)

    context = {
        'gender': gender
    }

    return render(request, 'gender/show.html', context)

def gender_create(request):
    return render(request, 'gender/create.html')

def gender_store(request):
    gender = request.POST.get('gender')

    if not gender:
        return render(request, 'gender/create.html', {'error_gender_field': 'Gender field is required.'})
    else:
        Gender.objects.create(gender=gender).save()

        messages.success(request, 'Gender successfully saved.')
        return redirect('/genders')
    
def gender_edit(request, id):
    gender = Gender.objects.get(pk=id)

    context = {
        'gender': gender
    }

    return render(request, 'gender/edit.html', context)

def gender_update(request, id):
    gender_obj = Gender.objects.get(pk=id)
    gender = request.POST.get('gender')
    
    if not gender:
        return render(request, 'gender/edit.html', {'error_gender_field': 'Gender field is required.'})
    else:
        gender_obj.gender = gender
        gender_obj.save()

        messages.success(request, 'Gender successfully updated.')
        return redirect('/genders')
    
def gender_delete(request, id):
    gender = Gender.objects.get(pk=id)

    context = {
        'gender': gender
    }

    return render(request, 'gender/delete.html', context)

def gender_destroy(request, id):
    gender = Gender.objects.get(pk=id)
    gender.delete()

    messages.success(request, 'Gender successfully deleted!')
    return redirect('/genders')

def user_index(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'user/index.html', context)

def user_create(request):
    genders = Gender.objects.select_related('gender').all()

    context = {
        'genders': genders
    }

    return render(request, 'user/create.html', context)

def user_store(request):
    genders = Gender.objects.all()

    context = {
        'genders': genders,
        'post_data': request.POST,
    }

    first_name = request.POST.get('first_name')
    middle_name = request.POST.get('middle_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    gender_id = request.POST.get('gender_id')
    birth_date = request.POST.get('birth_date')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if not first_name:
        context['first_name_required'] = 'The first name field is required.'
    
    if not last_name:
        context['last_name_required'] = 'The last name field is required.'

    if not age:
        context['age_required'] = 'The age field is required.'
    elif not age.isnumeric():
        context['age_numeric'] = 'The age field must be a number.'

    if not gender_id:
        context['gender_id_required'] = 'The gender field is required.'

    if not birth_date:
        context['birth_date_required'] = 'The birth date field is required.'
    
    if not username:
        context['username_required'] = 'The username field is required.'
    else:
        if User.objects.filter(username=username).exists():
            context['username_exists'] = 'The username is already taken.'

    if not password:
        context['password_required'] = 'The password field is required.'

    if not confirm_password:
        context['confirm_password_required'] = 'The confirm password field is required.'

    if password != confirm_password:
        context['password_mismatch'] = 'The password do not match.'

    if any(key in context for key in ['first_name_required', 'last_name_required', 'age_required', 'age_numeric', 'gender_id_required', 'birth_date_required', 'username_required', 'username_exists', 'password_required', 'confirm_password_required', 'password_mismatch']):
        return render(request, 'user/create.html', context)
    else:
        hashed_password = make_password(password)

        User.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, age=age, gender_id=gender_id, birthdate=birth_date, username=username, password=hashed_password)

        messages.success(request, 'User successfully saved!')

        return redirect('/users')