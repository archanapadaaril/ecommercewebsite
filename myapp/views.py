from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,product,Relatedimage,Cart
from .forms import SignupForm,SigninForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import decimal
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect("signin")
            messages.success(request,"User saved")
            
        else:
            messages.error(request,"Error in form")

    else:
        form=SignupForm()
    context={"form":form}
    return render(request,'signup.html',context)

def signin(request):
    if request.method=='POST':
        form=SigninForm(request.POST)
        
        username=form["username"].value()
        password=form["password"].value()
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect("/")
        else:
            messages.error(request,"Invalid Username or Password")
    else:
        form=SigninForm()
    context={"form":form}
    return render(request,'signin.html',context)


def about(request):
    return render(request,'about.html')

def categorypage(request):
    category=Category.objects.filter(is_active=True)
    return render(request,'category.html',{'category':category})



def categoryproduct(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=product.objects.filter(is_active=True,category=category)
    context={
        'category':category,
        'products':products,
    }
    return render(request,'category-product.html',context)

def contact(request):
    return render(request,'contact.html')

def productdetail(request):
    return render(request,'product-detail.html')



def blog(request):
    return render(request,'blog.html')

def blogdetail(request):
    return render(request,'blog-detail.html')

def detail_page(request,slug):
    detail=get_object_or_404(product,slug=slug,)
    relatedimages=Relatedimage.objects.filter(products=detail.id)

    context={
        'detail': detail,
        'relatedimages' : relatedimages,
    }
    return render(request,'detail.html',context)
@login_required
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    products=get_object_or_404(product,id=product_id)
    item_already_in_cart=Cart.objects.filter(products=product_id,user=user)
    if item_already_in_cart:
        cp=get_object_or_404(Cart,products=product_id,user=user)
        cp.quantity +=1
        cp.save()
    else:
        Cart(user=user,products=products).save()
    return redirect('shopingcart')

@login_required
def shopingcart(request):
    user=request.user
    cart_products=Cart.objects.filter(user=user)
    amount=decimal.Decimal(0)
    shipping_amount=decimal.Decimal(10)
    cp=[p for p in Cart.objects.all() if p.user==user]
    if cp:
        for p in cp:
            temp_amount=(p.quantity*p.products.price)
            amount += temp_amount

    context={
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount+shipping_amount,
    }
    return render(request,'shoping-cart.html',context)
@login_required
def pluscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.quantity +=1
        if cp.quantity>=cp.products.productStock:
            cp.quantity -=1
        cp.save()
    return redirect('shopingcart')

@login_required
def minuscart(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        if cp.quantity==1:
            cp.delete()
        else:
            cp.quantity-=1
            cp.save()
    return redirect('shopingcart')
@login_required
def delete(request,cart_id):
    if request.method=='GET':
        cp=get_object_or_404(Cart,id=cart_id)
        cp.delete()
    return redirect('shopingcart')

def logoutpage(request):
    logout(request)
    return redirect('/')





