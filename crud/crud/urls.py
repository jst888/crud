from django.conf.urls import url
from django.contrib import admin
from django.urls import path
import customers.views


admin.site.site_header = "CRUD Customers"
admin.site.site_title = "Customer"
admin.site.index_title = "Welcome to CRUD Customer List"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', customers.views.home, name='home'),
]
