

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse ,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from user_data.models import skill, Education, Project, Experience
from user_account.models import Profile
from django.conf import settings
from django.core.mail import send_mail
import math, random


from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    user_profile = Profile.objects.filter().all()
    # user_skill= skill.objects.filter().all()
    # user_edu= Education.objects.filter().all()
    # user_project= Project.objects.filter(user_id=id).all()
    # user_exp= Experience.objects.filter(user_id=id).all()
    return render(request, 'home.html', {'user_profile': user_profile})


def sign_in(request):
    try:
        if request.method == 'POST':

            email = request.POST['email']
            password = request.POST['password']

            user_obj = User.objects.filter(username=email)

            if user_obj:

                messages.error(request, f"Username is allready exists:{email}")
                return redirect('/login')
            else:
                user_obj = User.objects.create_user(
                    username=email, password=password, email=email)

                messages.success(request, f"New account created: {email}")
                return redirect('/login/')

        return render(request, 'sigin.html')

    except Exception as e:
        print(e)
        return HttpResponse("error")


def log_in(request):
    try:
        if request.user.is_authenticated:
            print("allready login")
            return redirect('/up_dashboard')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user_obj = User.objects.filter(username=username)
            user_obj = authenticate(username=username, password=password)
            # contant = {username:username}
            # if user_obj and user_obj.is_user:
            if user_obj:
                login(request, user_obj)
                url = "/up_dashboard"
                return redirect(url)

        return render(request, 'login.html')

    except Exception as e:
        print(e)


def logout_view(request):
    logout(request)
    # return render(request,'login.html')
    return redirect('/login/')


def dashboard(request, id):
    if request.user.is_authenticated:
        username = request.user

    user = User.objects.filter(username=id).all()
    print(user)
    for j in user:
        i = j

    user_profile = Profile.objects.filter(user_id=i).all()
    user_skill = skill.objects.filter(user_id=i).all()
    user_edu = Education.objects.filter(user_id=i).all()
    user_project = Project.objects.filter(user_id=i).all()
    user_exp = Experience.objects.filter(user_id=i).all()
    return render(request, 'user_dashboard.html', {'user_profile': user_profile, 'user_skill': user_skill, 'user_edu': user_edu, 'user_project': user_project, 'user_exp': user_exp})


@login_required(login_url='/login')
def up_dashboard(request):
    if request.user.is_authenticated:
        username = request.user
        print(type(username))
        h = settings.ALLOWED_HOSTS[2]
        h = "{h}/dashboard/{u}/".format(h=h, u=username)
        user_profile = Profile.objects.filter(user=username).all()
        user_skill = skill.objects.filter(user=username).all()
        user_edu = Education.objects.filter(user=username).all()
        user_project = Project.objects.filter(user=username).all()
        user_exp = Experience.objects.filter(user=username).all()

    return render(request, 'userup_dashboard.html', {'h': h, 'user_profile': user_profile, 'user_skill': user_skill, 'user_edu': user_edu, 'user_project': user_project, 'user_exp': user_exp})


def com(request):
    # logout(request)
    return render(request, 'components.html')


@login_required(login_url='/login')
def education_add(request):
    if request.user.is_authenticated:
        username = request.user

        if request.method == 'POST':
            c_name = request.POST['c_name']
            school_name = request.POST['school_name']
            Grade = request.POST['grade']
            description = request.POST['description']

            edu = Education(
                user_id=username.id,
                c_name=c_name,
                school_name=school_name,

                description=description,
                Grade=Grade
            )
            edu.save()
            return redirect('/up_dashboard')
    return render(request, 'userup_dashboard.html')


@login_required(login_url='/login')
def edu_delete(request):
    if request.user.is_authenticated:
        username = request.user
        user_edu = Education.objects.filter(user=username).all()

    if request.method == 'POST':
        c_name = request.POST['c']
        user_edu = Education.objects.filter(c_name=c_name).delete()
        return redirect('/up_dashboard')
    return render(request, 'userup_dashboard.html', {'user_edu': user_edu})


@login_required(login_url='/login')
def project_add(request):
    if request.user.is_authenticated:
        username = request.user

        if request.method == 'POST':
            project_name = request.POST['project_name']
            link = request.POST['project_link']
            image = request.FILES.get('project_Image')
            description = request.POST['description']

            edu = Project(
                user_id=username.id,
                project_name=project_name,
                company_name=link,
                description=description,
                image=image,

            )
            edu.save()
            return redirect('/up_dashboard')

    return render(request, 'userup_dashboard.html')


@login_required(login_url='/login')
def project_edit(request):
    if request.user.is_authenticated:
        username = request.user
        user_pro = Project.objects.filter(user=username).all()
        if request.method == 'POST':
            c_name = request.POST['c_name']
            school_name = request.POST['school_name']
            image = request.FILES.get('image')
            description = request.POST['description']

            edu = Project.objects.filter(c_name=c_name).update(

                user_id=username.id,
                project_name=c_name,
                company_name=school_name,

                image=image,
                description=description,
            )

            return redirect('/up_dashboard')

    return render(request, 'userup_dashboard.html', {'user_edu': user_pro})


@login_required(login_url='/login')
def project_delete(request):
    if request.user.is_authenticated:
        username = request.user
        user_pro = Project.objects.filter(user=username).all()

    if request.method == 'POST':
        c_name = request.POST['c']
        user_pro = Project.objects.filter(project_name=c_name).delete()
        return redirect('/up_dashboard')
    return render(request, 'userup_dashboard.html', {'user_edu': user_pro})


@login_required(login_url='/login')
def exp_add(request):
    if request.user.is_authenticated:
        username = request.user

        if request.method == 'POST':
            c_name = request.POST['c_name']
            school_name = request.POST['school_name']

            description = request.POST['description']

            edu = Experience(
                user_id=username.id,
                post_name=c_name,
                company_name=school_name,

                description=description,

            )
            edu.save()
            return redirect('/up_dashboard')

    return render(request, 'userup_dashboard.html')


@login_required(login_url='/login')
def exp_delete(request):
    if request.user.is_authenticated:
        username = request.user
        user_edu = Experience.objects.filter(user=username).all()

    if request.method == 'POST':
        c_name = request.POST['c']
        user_edu = Experience.objects.filter(post_name=c_name).delete()
        return redirect('/up_dashboard')
    return render(request, 'userup_dashboard.html', {'user_edu': user_edu})


@login_required(login_url='/login')
def skill_add(request):
    if request.user.is_authenticated:
        username = request.user

        if request.method == 'POST':
            c_name = request.POST['c_name']

            skilladd = skill(
                user_id=username.id,
                s_name=c_name,

            )
            skilladd.save()
            return redirect('/up_dashboard')

    return render(request, 'userup_dashboard.html')


@login_required(login_url='/login')
def skill_delete(request):
    if request.user.is_authenticated:
        username = request.user
        user_edu = skill.objects.filter(user=username).all()

    if request.method == 'POST':
        s_name = request.POST['c']
        user_skill = skill.objects.filter(s_name=s_name).delete()
        return redirect('up_dashboard')
    return render(request, 'userup_dashboard.html', {'user_skill': user_skill})


@login_required(login_url='/login')
def profile_edit(request):
    if request.user.is_authenticated:
        username = request.user

        print(username)
        if request.method == 'POST':

            name = request.POST['name']
            tagline = request.POST['tagline']
            About = request.POST['about']

            user_profile = Profile.objects.filter(user=username).all()
            if user_profile:
                print("user is persent")
                Profile.objects.filter(user_id=username.id).update(
                    user_id=username.id,
                    name=name,
                    tagline=tagline,
                    About=About
                )
            else:
                Profile.objects.filter(user_id=username.id).create(

                    user_id=username.id,
                    name=name,
                    tagline=tagline,
                    About=About
                )

        return redirect('/up_dashboard')

    return render(request, 'userup_dashboard.html', {'user_profile': user_profile})


def forgot_password(request):
    try:
        if request.method == 'POST':

            email = request.POST['email']
            print(email)
            
            user = User.objects.get(email=email)
            if not user:
                print("user is not persent")
                message = "user is not persent"
                return redirect("/sign_in")


                
            if user:
                print("user is persent")
                digits = "0123456789"
                OTP = ""

                    # length of password can be changed
                        # by changing value in range
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                subject = 'otp for password reset'
                message =f"email: {email}\n\nMessage:\n OTP is :{OTP}"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]

                print(email)
                send_mail(subject, message, from_email, recipient_list)    

                request.session['otp'] = OTP
                request.session['email'] = email    
                return  redirect('verify_otp')
                
            message = "email not exist"
            
        return render(request,'forgot_password.html')
    except Exception as e:
                
                
        print(e)
                
    



    


def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST['OTP']
        new_password = request.POST['password']
        print(otp)
        print(request.session.get('otp'))
        if otp == request.session.get('otp'):
            email = request.session.get('email')
            user = User.objects.get(email=email)
            # Generate a new password for the user or redirect them to a password reset page
            # Implement your code to handle the password reset here
            # For example:
            user.set_password(new_password)
            user.save()
            return redirect('/login/')
        else:
            
            return HttpResponse("verify_otp not match")
            
    
    return render(request, 'verify_otp.html')