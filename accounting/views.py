from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import AccountingEntries, Counterparty
from .tables import CounterpartyTable, CounterpartyAccountTable
from .helpers import acc_60_01, acc_60_02, acc_62_02, acc_62_01
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView


def excel_upload_accounting(request):
    acc_60_01()
    acc_60_02()
    acc_62_02()
    acc_62_01()
    return HttpResponse("Success")


class AccountsReview(SingleTableMixin, FilterView):
    model = Counterparty
    table_class = CounterpartyTable
    template_name = 'accounting/table.html'
    # filterset_class = ClientsListFilter
    table_pagination = {"per_page": 10}

    def get_table_kwargs(self):
        kwargs = super().get_table_kwargs()
        kwargs['order_by'] = '-accounts_receivables'
        return kwargs


def counterparty_details(request, pk):
    counterparty = Counterparty.objects.get(id=pk)
    accounts_payables = AccountingEntries.objects.filter(counterparty_id=pk)
    context = {"counterparty": counterparty, "accounts_payables": accounts_payables}
    return render(request, 'accounting/counterparty_details.html', context)


def clean_entries(request):
    entries = AccountingEntries.objects.all()
    entries.delete()
    return HttpResponse("Success")


class ReportAccountsReceivables(SingleTableMixin, FilterView):
    model = Counterparty
    table_class = CounterpartyAccountTable
    template_name = 'accounting/table_accounts.html'
    # filterset_class = ClientsListFilter
    table_pagination = {"per_page": 10}

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_table_data(self):
        data = self.get_queryset()
        for counterparty in data:
            oldest_date = counterparty.get_oldest_entry_date()
        return data

    def get_table_kwargs(self):
        kwargs = super().get_table_kwargs()
        kwargs['order_by'] = '-accounts_receivables'
        return kwargs





