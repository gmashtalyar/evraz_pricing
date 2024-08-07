import django_tables2 as tables
from .models import Counterparty, AccountingEntries
from django_tables2.utils import A
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.formats import date_format


class CounterpartyTable(tables.Table):
    counterparty = tables.LinkColumn('accounting:counterparty_details', args=[A('pk')], verbose_name='Контрагент', attrs={"td": {"id": lambda record: record.counterparty, "class": 'counterparty'}})
    # counterparty = tables.Column(verbose_name='Контрагент')
    accounts_receivables = tables.Column(verbose_name="ДЗ")
    accounts_payables = tables.Column(verbose_name="КЗ")
    advances_received = tables.Column(verbose_name="Авансы полученные")
    advances_paid = tables.Column(verbose_name="Авансы выданные")

    def render_accounts_receivables(self, value):
        return intcomma(value)

    def render_accounts_payables(self, value):
        return intcomma(value)

    def render_advances_received(self, value):
        return intcomma(value)

    def render_advances_paid(self, value):
        return intcomma(value)

    class Meta:
        model = Counterparty
        template_name = "django_tables2/bootstrap4.html"
        fields = ("counterparty", "accounts_receivables", "accounts_payables", "advances_received", "advances_paid")
        attrs = {
            'class': 'ui blue compact striped selectable celled table',
        }


class CounterpartyAccountTable(tables.Table):
    counterparty = tables.LinkColumn('accounting:counterparty_details', args=[A('pk')], verbose_name='Контрагент', attrs={"td": {"id": lambda record: record.counterparty, "class": 'counterparty'}})
    accounts_receivables = tables.Column(verbose_name="ДЗ")
    oldest_entry_date = tables.Column(verbose_name="Oldest Entry Date")

    def render_accounts_receivables(self, value):
        return intcomma(value)

    def render_oldest_entry_date(self, record):
        print(f"Rendering oldest entry date for counterparty: {record.counterparty}")
        oldest_date = record.get_oldest_entry_date()
        print(f"Oldest date: {oldest_date}")
        if oldest_date:
            return date_format(oldest_date, "SHORT_DATE_FORMAT")
        return "N/A"

    class Meta:
        model = Counterparty
        template_name = "django_tables2/bootstrap4.html"
        fields = ("counterparty", "accounts_receivables", "oldest_entry_date")
        attrs = {'class': 'ui blue compact striped selectable celled table',}
