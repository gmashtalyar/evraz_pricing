from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'pricing'

urlpatterns = [
    path('marketing-inputs/', views.marketing_inputs_form, name='marketing_inputs_form'),
    path('update-price/', views.update_price, name='update_price'),
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('upload_excel_3/', views.upload_excel_3, name='upload_excel_3'),
    path('update-price2/', views.update_price2, name='update_price2'),
    path('update-price3/', views.update_price3, name='update_price3'),
    path('marketing-inputs2/', views.marketing_inputs_form2, name='marketing_inputs_form2'),
    path('marketing-inputs3/', views.marketing_inputs_form3, name='marketing_inputs_form3'),
    path('', views.marketing_inputs_form3, name='marketing_inputs_form3'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
