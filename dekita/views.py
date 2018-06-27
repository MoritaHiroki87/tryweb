from django.urls import reverse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from dekita.models import ToDoList, Category
from dekita.forms import AddForm, AddCategoryForm


# Create your views here.


def index(request):
    todolist = ToDoList.objects.order_by("created_at")
    category = Category.objects.all()
    context = {"todolist": todolist,
               "category": category}

    return render(request, 'dekita/index.html', context)


def add(request):

    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = AddForm()
    context = {"form": form}

    return render(request, 'dekita/add.html', context)


def add_category(request):

    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = AddCategoryForm()
    context = {"form": form}

    return render(request, 'dekita/add_category.html', context)


def edit(request, todo_id):
    try:
        todo = ToDoList.objects.get(id=todo_id)
    except ToDoList.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = AddForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dekita:edit',
                                                args=(todo.id,)))
    else:
        form = AddForm(instance=todo)

        return TemplateResponse(request, "dekita/edit.html", {"form": form,
                                                              "todo": todo})


def done(request, todo_id):
    try:
        todolist = ToDoList.objects.get(id=todo_id)
    except ToDoList.DoesNotExist:
        raise Http404

    # if request.method == 'POST':
        # todolistの内容を完了リストに移す
    todolist.delete()
    return HttpResponseRedirect(reverse('dekita:index'))
    # else:
    #    return TemplateResponse(request, 'dekita:index')

