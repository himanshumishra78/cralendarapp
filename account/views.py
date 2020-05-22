from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserAddtnlForm,UpdateEmailForm
from .models import UserReg
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.core import serializers

# Create your views here.
def register(request):
    # search_form=SearchForm()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        user_addtnl_form=UserAddtnlForm(request.POST)
        if user_form.is_valid() and user_addtnl_form.is_valid():
            if len(user_form.cleaned_data['username'])<6 or len(user_form.cleaned_data['password'])<6:
                messages.error(request, "Username/Password should be at least 6 characters long")
                return render(request,'register.html',
                            {'user_form':user_form,
                            'user_addtnl_form':user_addtnl_form,
                            })
            elif len(str(user_addtnl_form.cleaned_data['mobile_num']))<10:
                messages.error(request, "Enter a valid mobile number")
                return render(request,'register.html',
                            {'user_form':user_form,
                            'user_addtnl_form':user_addtnl_form,
                            })
                return  render(request,'register.html',
                            {'user_form':user_form,
                            'user_addtnl_form':user_addtnl_form,
                            })
            new_user = user_form.save(commit="False")
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Create the user profile
            user_reg_obj=UserReg.objects.create(user=new_user,mobile_num=user_addtnl_form.data['mobile_num'])
            # user_reg_obj=user_addtnl_form.save()
            return render(request,'register_done.html',
            {'new_user':new_user})

    else:
        user_form=UserRegistrationForm()
        user_addtnl_form=UserAddtnlForm()
    return render(request,'register.html',
                {'user_form':user_form,
                'user_addtnl_form':user_addtnl_form,
                })

@login_required
def update_email(request):

    if request.method == 'POST':
        update_email_form=UpdateEmailForm(request.POST)
        if update_email_form.is_valid():
            cd=update_email_form.cleaned_data
            if cd['email'] != cd['confirm_email']:
                messages.error(request,'Emails do not match')
                return redirect('update_email')
            else:
                User.objects.update_or_create(username=request.user.username,
                                        defaults={'email':cd['email']})
                messages.error(request, "Email address Update successful")
                return redirect('products:index')
    else:
        update_email_form=UpdateEmailForm()
    try:
        cart_obj=get_object_or_404(Cart,user=request.user)
    except:
        cart_obj='null'
        pass
    return render(request,'update_email.html',{'update_email_form':update_email_form,
                                                'cart_obj':cart_obj,
                                                })
