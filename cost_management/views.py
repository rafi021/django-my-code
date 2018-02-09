from django.shortcuts import render ,redirect
from . models import Expense
from .forms import ExpenseForm

# Create your views here.
def my_expense(request):
    expenses = Expense.objects.all()
    total = 0
    for expense in expenses:
        total += expense.amount
    context = {
        'expenses': expenses,
        'total': total,
    }
    return render(request, 'cost/expense.html', context)

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect('cost-list')
    else:
        form = ExpenseForm
    context = {'form': form, }
    return render(request, 'cost/add_expense.html', context)

def edit_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        form.save()
        return redirect('cost-list')
    else:
        form = ExpenseForm(instance=expense)
    context = {'form': form, }
    return render(request, 'cost/edit_expense.html', context)

def delete_expense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('cost-list')
