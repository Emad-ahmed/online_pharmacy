from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from mediapp.models import Product
from django.views.generic.base import View
from medihubbd.settings import MEDIA_URL
from django.urls import path
from mediapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.show_cart, name='show_cart'),
    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('addproduct/', views.Addproduct.as_view(), name='addproduct'),
    path('doctor/', views.doctor, name='doctor'),
    path('venue_pdf', views.venue_pdf, name='venue_pdf'),
    path('buy/<int:id>', views.buy_now, name='buy'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('orders_delete/<int:id>/', views.orders_delete, name='orders_delete'),
    path('prescription_order/', views.prescription_order,
         name='prescription_order'),
    path('devices/', views.devices, name='devices'),
    path('ambulance/', views.AmbulanceView.as_view(), name='ambulance'),
    path('addambulance/', views.addAmbulanceView.as_view(), name='addambulance'),
    path('covid/', views.covid, name='covid'),
    path('coviddata/<slug:data>', views.covid, name='coviddata'),
    path('covidinformation/', views.covidinformation, name='covidinformation'),
    path('Herbal/', views.Herbal, name='Herbal'),
    path('BabyMom/', views.BabyMom, name='BabyMom'),
    path('Nutrition/', views.Nutrition, name='Nutrition'),
    path('PersonalCare/', views.PersonalCare, name='PersonalCare'),
    path('otc/', views.OTC, name='otc'),
    path('Prescription/', views.Prescription, name='Prescription'),
    path('add_doctor/', views.DoctorADD.as_view(), name='add_doctor'),
    path('doctor_details/<int:id>/', views.doctor_details, name='doctor_details'),
    path('delete_ticket/<int:id>/', views.delete_ticket, name='delete_ticket'),
    path('addbkash', views.addbkash, name='addbkash'),
    path('checkout/', views.checkout, name='checkout'),
    path('Healtcare/', views.Healtcare, name='Healtcare'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('buypaymentdone/', views.buy_payment_done, name='buypaymentdone'),
    path('searchhresult', views.searchhresult, name='searchhresult'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', views.PasswordChangeView.as_view(),
         name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    # Password Reset


    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),


    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),


    path('password-reset-complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_done.html'), name='password_reset_complete'),


    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),

    path('deletecart/<int:id>/', views.deletecart,
         name='deletecart'),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
