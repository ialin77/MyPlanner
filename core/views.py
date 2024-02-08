from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plan.models import Plan


def homepage(request):
    return render(request, 'core/index.html')


@login_required(login_url='login')
def my_plans(request):
    current_user = request.user.id

    plans = Plan.objects.all().filter(user=current_user)

    context = {'plans': plans}
    return render(request, 'core/my_plans.html', context)




