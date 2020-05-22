from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    logged_users = LoggedUser.objects.all().order_by('username')
    return render(request,"index.html",{
        'logged_users':logged_users,
    }
    )
