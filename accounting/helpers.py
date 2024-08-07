import pandas as pd
from .models import AccountingEntries, Counterparty
from django.db.models import Sum


def acc_62_01():
    dates_list = ["Дата"]
    ending_account = "Дебет.2"
    df = pd.read_excel("Documents/accounts.xlsx", sheet_name="62.01 ДЗ", parse_dates=dates_list, skiprows=1)
    df = df.drop(df.index[:2])
    selected_columns = ['Документы расчетов с контрагентом', 'Дата', 'Склад', 'Договор', 'Контрагент', ending_account]
    df = df[selected_columns]
    df = df[df["Контрагент"].notna()]
    df[ending_account].fillna(0, inplace=True)

    for index, row in df.iterrows():
        counterparty_name = row['Контрагент']
        counterparty, created = Counterparty.objects.get_or_create(counterparty=counterparty_name,
               defaults={'accounts_receivables': 0, 'accounts_payables': 0, "advances_received": 0, "advances_paid": 0})

        AccountingEntries.objects.create(account="62.01", document=row['Документы расчетов с контрагентом'],
                date=row['Дата'], sklad=row['Склад'], contract=row['Договор'], counterparty=counterparty, value=row[ending_account])
    for counterparty in Counterparty.objects.all():
        total_value = AccountingEntries.objects.filter(counterparty=counterparty).filter(account="62.01").aggregate(total_value=Sum('value'))['total_value']
        if total_value is not None:
            counterparty.accounts_receivables = total_value
            counterparty.save()


def acc_60_01():
    dates_list = ["Дата"]
    ending_account = "Кредит.2"
    df = pd.read_excel("Documents/accounts.xlsx", sheet_name="60.01 КЗ", parse_dates=dates_list, skiprows=1)
    df = df.drop(df.index[:2])
    selected_columns = ['Документы расчетов с контрагентом', 'Дата', 'Склад', 'Договор', 'Контрагент',
                        ending_account]
    df = df[selected_columns]
    df = df[df["Контрагент"].notna()]
    df[ending_account].fillna(0, inplace=True)

    for index, row in df.iterrows():
        counterparty_name = row['Контрагент']
        counterparty, created = Counterparty.objects.get_or_create(counterparty=counterparty_name,
               defaults={'accounts_receivables': 0, 'accounts_payables': 0, "advances_received": 0, "advances_paid": 0})

        AccountingEntries.objects.create(account="60.01", document=row['Документы расчетов с контрагентом'],
                                         date=row['Дата'], sklad=row['Склад'], contract=row['Договор'],
                                         counterparty=counterparty, value=row[ending_account])
    for counterparty in Counterparty.objects.all():
        total_value = AccountingEntries.objects.filter(counterparty=counterparty).filter(account="60.01").aggregate(
            total_value=Sum('value'))['total_value']
        if total_value is not None:
            counterparty.accounts_payables = total_value
            counterparty.save()


def acc_62_02():
    dates_list = ["Дата"]
    ending_account = "Кредит.2"
    df = pd.read_excel("Documents/accounts.xlsx", sheet_name="62.02 авансы полученные", parse_dates=dates_list, skiprows=1)
    df = df.drop(df.index[:2])
    selected_columns = ['Документы расчетов с контрагентом', 'Дата', 'Склад', 'Договор', 'Контрагент', ending_account]
    df = df[selected_columns]
    df = df[df["Контрагент"].notna()]
    df[ending_account].fillna(0, inplace=True)

    for index, row in df.iterrows():
        counterparty_name = row['Контрагент']
        counterparty, created = Counterparty.objects.get_or_create(counterparty=counterparty_name,
               defaults={'accounts_receivables': 0, 'accounts_payables': 0, "advances_received": 0, "advances_paid": 0})

        date_value = row['Дата']
        if isinstance(date_value, str):
            date_value = pd.to_datetime(date_value, errors='coerce')

        AccountingEntries.objects.create(account="62.02", document=row['Документы расчетов с контрагентом'],
            date=date_value, sklad=row['Склад'], contract=row['Договор'], counterparty=counterparty,
             value=row[ending_account])
    for counterparty in Counterparty.objects.all():
        total_value = AccountingEntries.objects.filter(counterparty=counterparty).filter(account="62.02").aggregate(
            total_value=Sum('value'))['total_value']
        if total_value is not None:
            counterparty.advances_received = total_value
            counterparty.save()


def acc_60_02():
    dates_list = ["Дата"]
    ending_account = "Дебет.2"
    df = pd.read_excel("Documents/accounts.xlsx", sheet_name="60.02 авансы выданные", parse_dates=dates_list, skiprows=1)
    df = df.drop(df.index[:2])
    selected_columns = ['Документы расчетов с контрагентом', 'Дата', 'Склад', 'Договор', 'Контрагент',
                        ending_account]
    df = df[selected_columns]
    df = df[df["Контрагент"].notna()]
    df[ending_account].fillna(0, inplace=True)

    for index, row in df.iterrows():
        counterparty_name = row['Контрагент']
        counterparty, created = Counterparty.objects.get_or_create(counterparty=counterparty_name,
               defaults={'accounts_receivables': 0, 'accounts_payables': 0, "advances_received": 0, "advances_paid": 0})
        AccountingEntries.objects.create(account="60.02", document=row['Документы расчетов с контрагентом'],
                                         date=row['Дата'], sklad=row['Склад'], contract=row['Договор'],
                                         counterparty=counterparty, value=row[ending_account])
    for counterparty in Counterparty.objects.all():
        total_value = AccountingEntries.objects.filter(counterparty=counterparty).filter(account="60.02").aggregate(
            total_value=Sum('value'))['total_value']
        if total_value is not None:
            counterparty.advances_paid = total_value
            counterparty.save()
