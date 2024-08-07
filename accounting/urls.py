from django.urls import path
from . import views
from .views import AccountsReview, ReportAccountsReceivables
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounting'

urlpatterns = [
    # path('accounts/', views.accounts, name='accounts'),
    path('excel_upload_accounting/', views.excel_upload_accounting, name='excel_upload_accounting'),
    path('clean_entries/', views.clean_entries, name='clean_entries'),
    path('accounts/', AccountsReview.as_view(), name='accounts'),
    path('counterparty_details/<int:pk>', views.counterparty_details, name='counterparty_details'),
    path('accounts_receivables/', ReportAccountsReceivables.as_view(), name='accounts_receivables'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
