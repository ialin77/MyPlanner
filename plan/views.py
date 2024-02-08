from django.shortcuts import render, redirect
from .forms import CreatePlanForm
from django.contrib.auth.decorators import login_required
from .models import Plan




@login_required(login_url='login')
def add_plan(request):
    form = CreatePlanForm()

    if request.method == 'POST':
        form = CreatePlanForm(request.POST)

        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()

            return redirect('my_plans')

    context = {'form': form}
    return render(request, 'plan/add_plan.html', context)


@login_required(login_url='login')
def update_plan(request, pk):
    try:
        plan = Plan.objects.get(id=pk, user=request.user)
    except:
        return redirect('my_plans')

    form = CreatePlanForm(instance=plan)

    if request.method == 'POST':
        form = CreatePlanForm(request.POST, instance=plan)

        if form.is_valid():
            form.save()

            return redirect('my_plans')

    context = {'form': form}
    return render(request, 'plan/update_plan.html', context)



@login_required(login_url='login')
def delete_plan(request, pk):
    try:
        plan = Plan.objects.get(id=pk, user=request.user)
    except:
        return redirect('my_plans')

    if request.method == 'POST':
        plan.delete()

        return redirect('my_plans')

    return render(request, 'plan/delete_plan.html')
