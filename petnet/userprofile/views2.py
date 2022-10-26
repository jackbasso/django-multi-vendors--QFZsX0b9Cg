from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils.text import slugify
from .models import Userprofile
from store.forms import ProductForm
from store.models import Category, Product  

def vendor_detail(request, pk):
  user = User.objects.get(pk=pk)
  return render(request, 'userprofile/vendor_detail.html', { 'user':user})

@login_required
def my_store(request):
  return render(request, 'userprofile/mystore.html')

@login_required
def add_product(request):
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
      title = request.POST.get('title')
      product = form.save(commit=False)
      product.user = request.user
      product.slug = slugify(title)
      product.save()

      return redirect('my_store')
  else:
    form = ProductForm()

  return render(request, 'userprofile/add_product.html', { 'form':form, 'title':'Add product' })

@login_required
def edit_product(request, pk):
  product = Product.objects.filter(user=request.user).get(pk=pk)

  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
      return redirect('my_store')
  else:
    form = ProductForm(instance=product) # fill the form with product info
  return render(request, 'userprofile/add_product.html', { 'form':form, 'title':'Edit product' })

@login_required
def myaccount(request):
  return render(request, 'userprofile/myaccount.html')

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()

      login(request, user)

      userprofile = Userprofile.objects.create(user=user)
      return redirect('frontpage')
  else:
    form = UserCreationForm()
  
  return render(request, 'userprofile/signup.html', {'form':form})