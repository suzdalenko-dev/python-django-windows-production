"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from invoice.controllers import login_controller, registrer_controller, invoice_controller, default_controller, pdf_controller

urlpatterns = [
   path('register/', registrer_controller.try_register ),
   path('login/', login_controller.try_login),
   path('invoice/<str:action>/<int:id>', invoice_controller.invoice_actions),
   path('default/<str:action>/<str:entity>/<int:id>', default_controller.default_actions),
   path('pdf/<str:action>/<int:id>', pdf_controller.pdf_work ),
]
