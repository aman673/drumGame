from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from app1.models import *
from django.views.generic import CreateView
from django.http import Http404
# Create your views here.
from app1.forms import *
def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(data = request.POST)
        customer_form = CustomerCreateForm(data = request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            u = user_form.save()
            customer = customer_form.save(commit = False)
            customer.user = u
            customer.save()
            return redirect(reverse('login'))
        # print(user_form,customer_form)
        # process the data
    else:
        user_form = UserCreateForm()
        customer_form = CustomerCreateForm()
    return render(request,'register.html',{'user_form':user_form,
                                           'customer_form':customer_form})

def index(request):
    user = request.user
    return render(request,'index.html',{'user':user})

class ProductCreate(CreateView):
    form_class = ProductCreateForm
    template_name = 'app1/product_create.html'
    success_url = reverse_lazy('index')
    
    def form_validate(self,form):
        self.object = form.save(commit = False)
        if self.user.merchant:
            self.object.seller = self.request.user.merchant 
        else:
            return Http404
        self.object.save()
        return super(ProductCreate,self).form_valid(form)
    