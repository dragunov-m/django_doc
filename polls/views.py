from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
#from .forms import ProductForm


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


def product_company(request):
    create_companies()  # добавляем начальные данные для компаний

    # если запрос POST, сохраняем данные
    if request.method == "POST":
        product = Product()
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.company_id = request.POST.get("company")
        product.save()
        return HttpResponseRedirect("/polls/form")
    # передаем данные в шаблон
    companies = Company.objects.all()
    template = loader.get_template('polls/create.html')
    context = {
        'companies_list': companies
    }
    return HttpResponse(template.render(context, request))


def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name="Apple")
        Company.objects.create(name="Asus")
        Company.objects.create(name="MSI")
