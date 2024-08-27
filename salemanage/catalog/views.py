from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Catagory, Product, Customer, Order
from django.views import generic
from django.urls import reverse_lazy, reverse
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
import csv
from .forms import UpLoadFileForm
# Create your views here.
def index(request):
    num_catagory = Catagory.objects.all().count()
    num_product = Product.objects.all().count()
    num_customer = Customer.objects.all().count()
    num_order = Order.objects.all().count()
    context = {
        'num_catagory': num_catagory,
        'num_product': num_product,
        'num_customer':num_customer,
        'num_order': num_order
    }
    return render(request, 'index.html' ,context=context)

class CatagoryListView(generic.ListView):
    model = Catagory
class CatagoryDetailView(generic.DetailView):
    model = Catagory
class ProductListView(generic.ListView):
    model = Product
class ProductDetailView(generic.DetailView):
    model = Product
class CustomerListView(generic.ListView):
    model = Customer
class CustomerDetailView(generic.DetailView):
    model = Customer
class OrderListView(generic.ListView):
    model = Order
class OrderDetailView(generic.DetailView):
    model = Order
def CatagoryCreate(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        c_image = request.FILES.get('c_image')

        if c_image and c_name:
            Catagory.objects.create(c_name=c_name, c_image=c_image)
            return redirect('catagorys')
        else:
            return render(request, 'catalog/catagory_form.html', {
                'error': 'Error appears',
                'catagoty': Catagory()
            })
    return render(request, 'catalog/catagory_form.html', {'catagory':Catagory()})
def CatagoryUpdate(request,pk):
    catagory = get_object_or_404(Catagory, pk=pk)
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        c_image = request.FILES.get('c_image')

        if c_name:
            catagory.c_name = c_name
        if c_image:
            catagory.c_image = c_image
        catagory.save()
        return redirect('catagorys')
    return render(request, 'catalog/catagory_form.html', {'catagory':catagory})
def CatagoryDelete(request, pk):
    catagory = get_object_or_404(Catagory, pk=pk)
    if request.method == 'POST':
        catagory.delete()
        return redirect('catagorys')
    return render(request, 'catalog/catagory_confirm_delete.html', {'catagory':catagory})

def ProductCreate(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_image = request.FILES.get('p_image')
        catagory_id = request.POST.get('catagory')
        price = float(request.POST.get('price'))

        catagory = get_object_or_404(Catagory, pk=catagory_id)
        if p_image and p_name and catagory and price:
            Product.objects.create(p_name=p_name, p_image=p_image, catagory=catagory, price=price)
            return redirect('products')
        else:
            return render(request, 'catalog/product_form.html', {
                'error': 'Error appears',
                'product': Product(),
                'catagorys': Catagory.objects.all()
            })
    return render(request, 'catalog/product_form.html', {'product':Product(), 'catagorys':Catagory.objects.all()})
def ProductUpdate(request,pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_image = request.FILES.get('p_image')
        catagory_id = request.POST.get('catagory')
        price = float(request.POST.get('price'))
        if p_name:
            product.p_name = p_name
        if p_image:
            product.p_image = p_image
        if catagory_id:
            catagory = get_object_or_404(Catagory, pk=catagory_id)
            product.catagory = catagory
        if price:
            product.price = price
        product.save()
        return redirect('products')
    return render(request, 'catalog/product_form.html', {'product':product, 'catagorys':Catagory.objects.all()})
def ProductDelete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'catalog/product_confirm_delete.html', {'product':product})
def CustomerCreate(request):
    if request.method == 'POST':
        cus_name = request.POST.get('cus_name')
        pkkh = request.POST.get('pkkh')
        created_date = request.POST.get('created_date')
        category_ids = request.POST.getlist('categories')
        product_ids = request.POST.getlist('products')

        
        if cus_name and pkkh and category_ids and product_ids and created_date:
            customer = Customer.objects.create(cus_name = cus_name, pkkh = pkkh, created_date = created_date)
            customer.categories.set(category_ids)
            customer.products.set(product_ids)
            return redirect('customers')
        else:
            return render(request, 'catalog/customer_form.html', {
                'error': 'Error appears',
                'customer': Customer(),
                'categories': Catagory.objects.all(),
                'products': Product.objects.all()
            })
    return render(request, 'catalog/customer_form.html', {'customer':Customer(), 'categories':Catagory.objects.all(), 'products':Product.objects.all()})
def CustomerUpdate(request,pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        cus_name = request.POST.get('cus_name')
        pkkh = request.POST.get('pkkh')
        created_date = request.POST.get('created_date')
        category_ids = request.POST.getlist('categories')
        product_ids = request.POST.getlist('products')
        if cus_name:
            customer.cus_name = cus_name
        if pkkh:
            customer.pkkh = pkkh
        if created_date:
            customer.created_date = created_date
        if category_ids:
            customer.categories.set(category_ids)
        if product_ids:
            customer.products.set(product_ids)
        customer.save()
        return redirect('customers')
    return render(request, 'catalog/customer_form.html', {'customer':customer, 'categories':Catagory.objects.all(), 'products':Product.objects.all()})
def CustomerDelete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')
    return render(request, 'catalog/customer_confirm_delete.html', {'customer':customer})
def OrderCreate(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        catagory_id = request.POST.get('catagory')
        product_id = request.POST.get('product')
        created_date = request.POST.get('created_date')
        count = int(request.POST.get('count'))

        catagory = get_object_or_404(Catagory, pk=catagory_id)
        customer = get_object_or_404(Customer, pk=customer_id)
        product = get_object_or_404(Product, pk=product_id)

        if  customer and catagory and product and count and created_date:
            order = Order.objects.create(customer = customer, catagory=catagory, product=product, count=count, created_date=created_date)
            order.total = order.count * order.product.price
            order.save()
            return redirect('orders')
        else:
            return render(request, 'catalog/order_form.html', {
                'error': 'Error appears',
                'order': Order(),
                'catagorys': Catagory.objects.all(),
                'customers': Customer.objects.all(),
                'products': Product.objects.all()
            })
    return render(request, 'catalog/order_form.html', {'order':Order(), 'catagorys':Catagory.objects.all(), 'products':Product.objects.all(), 'customers':Customer.objects.all()})
def OrderUpdate(request,pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        catagory_id = request.POST.get('catagory')
        product_id = request.POST.get('product')
        created_date = request.POST.get('created_date')
        count = int(request.POST.get('count'))

        catagory = get_object_or_404(Catagory, pk=catagory_id)
        customer = get_object_or_404(Customer, pk=customer_id)
        product = get_object_or_404(Product, pk=product_id)
        if customer_id:
            customer = get_object_or_404(Customer, pk=customer_id)
            order.customer = customer
        if catagory_id:
            catagory = get_object_or_404(Catagory, pk=catagory_id)
            order.catagory = catagory
        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            order.product = product
        if count:
            order.count = count
        if created_date:
            order.created_date = created_date
        order.total = order.count * order.product.price
        order.save()
        return redirect('orders')
    return render(request, 'catalog/order_form.html', {'order':order, 'catagorys':Catagory.objects.all(), 'customers': Customer.objects.all(), 'products': Product.objects.all()})
def OrderDelete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders')
    return render(request, 'catalog/order_confirm_delete.html', {'order':order})
def upload_file(request):
    if request.method == 'POST':
        file_form = UpLoadFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']
            reader = csv.reader(file.read().decode('utf-8').splitlines())
            header = next(reader)
            for row in reader:
                if not row or len(row)<len(header):
                    continue

                customer_name = row[header.index('Tên khách hàng')]
                catagory_name = row[header.index('Tên nhóm hàng')]
                product_name = row[header.index('Tên mặt hàng')]
                count_value = int(row[header.index('SL')])
                created_date_value = row[header.index('Thời gian tạo đơn')]
                price_value = float(row[header.index('Đơn giá')])
                pkkh_value = row[header.index('Mã PKKH')]

                customer = Customer.objects.filter(cus_name = customer_name).first()
                if customer:
                    catagory,_ = Catagory.objects.get_or_create(c_name = catagory_name)
                    product, product_create = Product.objects.get_or_create(
                        p_name = product_name,
                        defaults={'price':price_value, 'catagory': catagory}
                    )
                    if not product_create and product.price != price_value:
                        product.price = price_value
                        product.save()
                    customer.categories.add(catagory)
                    customer.products.add(product)
                else:
                    customer = Customer.objects.create(
                        pkkh=pkkh_value,
                        cus_name = customer_name
                    )
                    catagory,_ = Catagory.objects.get_or_create(c_name = catagory_name)
                    product, product_create = Product.objects.get_or_create(
                        p_name = product_name,
                        defaults={'price':price_value, 'catagory': catagory}
                    )
                    if not product_create and product.price != price_value:
                        product.price = price_value
                        product.save()
                    customer.categories.add(catagory)
                    customer.products.add(product)

                
                Order.objects.create(
                    customer=customer,
                    catagory=catagory,
                    product=product,
                    count=count_value,
                    created_date=created_date_value)
        return redirect('orders')
    else:
        file_form = UpLoadFileForm()
    return render(request, 'catalog/upload.html', {'file_form':file_form, 'order_list':Order.objects.all()})
            
