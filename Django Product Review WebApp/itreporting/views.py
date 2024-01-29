from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormView
from .forms import ContactForm  



def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'})      
        
def product(request):
    products_data = {'products': Product.objects.all(), 'title': 'Products Reported'}
    return render(request, 'itreporting/products.html', products_data)

class ProductListView(ListView):
    model = Product
    template_name = 'itreporting/products.html'
    context_object_name = 'details'
    ordering = ['-date_submitted']
    paginate_by = 5  # Add this line for pagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'itreporting/product_detail.html'
    context_object_name = 'product'
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'itreporting/product_form.html'
    fields = ['name', 'product_picture', 'manufacturer', 'average_cost', 'category', 'release_date', 'description', 'ratings']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('itreporting:product-detail', kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'product_picture', 'manufacturer', 'average_cost', 'category', 'release_date', 'description', 'ratings']

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.author

    def get_success_url(self):
        return reverse_lazy('itreporting:product-detail', kwargs={'pk': self.object.pk})
        
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('itreporting:products')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.author


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'itreporting/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context.update({'title': 'Contact Us'})
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Successfully sent the enquiry')
        form.send_mail()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Unable to send the enquiry')
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path
    