from django.shortcuts import render
from shop.models import Product, Customer, Order, OrderItem, ShippingAddress, Rubric
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from shop.forms import ContactForm
from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect
from django.db.models import Q 
from django.views.generic import TemplateView

class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'

class ProductListView(ListView):
	template_name = 'shop/home_page.html'
	context_object_name = 'products'
	model = Product
	paginate_by = 8

	def get_context_data(self, **kwargs):
		context = super(ProductListView, self).get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context

class ProductDetailView(DetailView):
	template_name = 'shop/product_detail.html'
	context_object_name = 'product'
	model = Product
	paginate_by = 4	

	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['rubrics'] = Rubric.objects.all()
		return context

def by_rubric(request, rubric_id):
    products = Product.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'products': products,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, 'shop/by_rubric.html', context)

def contact(request):
	submitted = False 
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['PracticeShaxruxPyDev.pythonanywhere.com'],
				connection = con
			)
			return HttpResponseRedirect('/contact?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form' : form,
		'product_list' : Product.objects.all(),
		'submitted' : submitted
	}
	return render(request, 'shop/contact.html', context)

def about(request):
	return render(request, 'shop/about.html')

class SearchResultView(ListView):
	model = Product
	template_name = 'shop/search_results.html'

	def get_queryset(self):
		query = self.request.GET.get("q")
		object_list = Product.objects.filter(
			Q(name__icontains=query)
		)
		return object_list