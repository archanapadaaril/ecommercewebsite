from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),

    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),

    path('about/',views.about,name='about'),

    path('category',views.categorypage,name='categorypage'),
    
    path('<slug:slug>/',views.categoryproduct,name='categoryproduct'),
    
    path('contact',views.contact,name='contact'),

    path('product-detail',views.productdetail,name='productdetail'),

    path('add_to_cart',views.add_to_cart,name='add_to_cart'),

    path('shoping-cart',views.shopingcart,name='shopingcart'),

    path('pluscart/<int:cart_id>/',views.pluscart,name='pluscart'),

    path('minuscart/<int:cart_id>/',views.minuscart,name='minuscart'),

    path('logoutpage',views.logoutpage,name='logoutpage'),

    path('delete/<int:cart_id>/',views.delete,name='delete'),

    path('blog',views.blog,name='blog'),

    path('blog-detail',views.blogdetail,name='blogdetail'),

    path('detail/<slug:slug>/',views.detail_page,name='detail_page')

    
]