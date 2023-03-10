from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import *


def index(request):
    question_text = Question.objects.all()
    # One to One
    single_user = User.objects.get(name='Sam')
    users_list = User.objects.all()
    # One to Many
    products_list = Product.objects.all()
    companies_list = Company.objects.all()
    # Many to Many
    courses_students = Course.objects.all()
    students_courses = Student.objects.all()

    template = loader.get_template('polls/index.html')
    context = {
        'question_text': question_text,
        # One to One
        'single_user': single_user,
        'users_list': users_list,
        # One to Many
        'companies_list': companies_list,
        'products_list': products_list,
        # Many to Many
        'courses_students': courses_students,
        'students_courses': students_courses,
    }
    return HttpResponse(template.render(context, request))


def form(request):
    products_list = Product.objects.order_by('name')
    template = loader.get_template('polls/form.html')
    context = {
        'products_list': products_list,
    }
    return HttpResponse(template.render(context, request))


def form_get(request):
    template = loader.get_template('polls/form_get.html')
    result = request.GET['result']
    context = {
        'result': result
    }
    return HttpResponse(template.render(context, request))


def add_product(request):

    create_companies()

    if request.method == 'POST':
        form_product = AddProductForm(request.POST)

        if form_product.is_valid():
            form_product.save()
            return redirect('polls:form')
    else:
        form_product = AddProductForm(request.GET)

        if form_product.is_valid():
            form_product.save()
            return redirect('polls:form')

    companies = Company.objects.all()

    return render(request, 'polls/create.html', {'form': form_product, 'companies_list': companies})


def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name="Apple")
        Company.objects.create(name="Asus")
        Company.objects.create(name="MSI")
