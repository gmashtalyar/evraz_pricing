from django.db import models
from django.db.models import Min


class Counterparty(models.Model):
    counterparty = models.CharField(max_length=250)
    accounts_receivables = models.BigIntegerField()
    accounts_payables = models.BigIntegerField()
    advances_received = models.BigIntegerField()
    advances_paid = models.BigIntegerField()

    def get_oldest_entry_date(self):
        oldest_entry = self.accounting_entries.aggregate(oldest_date=Min('date'))
        return oldest_entry['oldest_date']


class AccountingEntries(models.Model):
    counterparty = models.ForeignKey(Counterparty, on_delete=models.CASCADE, related_name='accounting_entries')
    account = models.CharField(max_length=10)
    document = models.CharField(max_length=250)
    date = models.DateTimeField()
    sklad = models.CharField(max_length=250)
    contract = models.CharField(max_length=250)
    value = models.BigIntegerField()



