from django import forms
from django.forms import ModelForm
from lib.models import Category, Person, Staff
from calc.models import Transaction
from salary.models import Worker
from bootstrap3_datetime.widgets import DateTimePicker
import datetime




class TransactionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        last_transaction = Transaction.objects.filter(
            creator__id=user_id).order_by('create_date').last()
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['money'].queryset = Staff.objects.get(
            name__id=user_id).pouches.all().order_by('name')
        self.fields['date'].initial = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        if last_transaction:
            self.fields['money'].initial = last_transaction.money
            self.fields['who_is'].initial = last_transaction.who_is
            self.fields['category'].initial = last_transaction.category

    error = {'required': 'Необходимо заполнить'}
    date = forms.DateTimeField(
        label="Дата",
        widget=DateTimePicker(
            options={"format": "YYYY-MM-DD HH:mm"}
        ),
        error_messages=error)
    sum_val = forms.IntegerField(
        label="Сумма",
        max_value=999999999,
        min_value=1
    )
    category = forms.ModelChoiceField(
        label="Категория",
        queryset=Category.objects.all().order_by('name'),
        error_messages=error
    )
    who_is = forms.ModelChoiceField(
        label="Персона",
        queryset=Person.objects.all().order_by('firstname'),
        error_messages=error
    )
    money = forms.ModelChoiceField(
        label="Счет",
        queryset=Staff.objects.none(),
        error_messages=error
    )
    comment = forms.CharField(
        label="Комментарий",
        max_length=50,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': '3',})
    )

class TransactionEditForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'sum_val', 'category', 'who_is', 'money', 'comment']

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(TransactionEditForm, self).__init__(*args, **kwargs)
        self.fields['money'].queryset = Staff.objects.get(
            name__id=user_id).pouches.all().order_by('name')
        self.fields['date'] = forms.DateTimeField(
            label="Дата", widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
        self.fields['comment'].widget = forms.Textarea(attrs={'rows': '3',})

class MonthForm(forms.Form):
    month = (
        ('',''),
        ('1', 'Январь'),
        ('2', 'Февраль'),
        ('3', 'Март'),
        ('4', 'Апрель'),
        ('5', 'Май'),
        ('6', 'Июнь'),
        ('7', 'Июль'),
        ('8', 'Август'),
        ('9', 'Сетнябрь'),
        ('10', 'Октябрь'),
        ('11', 'Ноябрь'),
        ('12', 'Декабрь')
    )
    year = (
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
	('2020', '2020')
    )
    select_month = forms.ChoiceField(choices=month, label="Выбрать другой месяц")
    select_year = forms.ChoiceField(choices=year, initial='2020')


class WorkReportTransactionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        report = kwargs.pop('report', None)
        user_id = kwargs.pop('user_id', None)
        last_transaction = Transaction.objects.filter(
            creator_id=user_id).order_by('create_date').last()
        super(WorkReportTransactionForm, self).__init__(*args, **kwargs)
        self.fields['sum_val'].initial = report.income
        self.fields['money'].queryset = Staff.objects.get(
            name__id=user_id).pouches.all().order_by('name')
        self.fields['date'] = forms.DateTimeField(
            label="Дата", widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm"}))
        self.fields['comment'].widget = forms.Textarea(attrs={'rows': '3', })
        self.fields['date'].initial = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.fields['category'].initial = report.work.category
        self.fields['who_is'].initial = Worker.objects.get(user=report.user).name
        if last_transaction:
            self.fields['money'].initial = last_transaction.money

    error = {'required': 'Необходимо заполнить'}
    date = forms.DateTimeField(
        label="Дата",
        widget=DateTimePicker(
            options={"format": "YYYY-MM-DD HH:mm"}
        ),
        error_messages=error)
    sum_val = forms.IntegerField(
        label="Сумма",
        max_value=999999999,
        min_value=1
    )
    category = forms.ModelChoiceField(
        label="Категория",
        queryset=Category.objects.all().order_by('name'),
        error_messages=error
    )
    who_is = forms.ModelChoiceField(
        label="Персона",
        queryset=Person.objects.all().order_by('firstname'),
        error_messages=error
    )
    money = forms.ModelChoiceField(
        label="Счет",
        queryset=Staff.objects.none(),
        error_messages=error
    )
    comment = forms.CharField(
        label="Комментарий",
        max_length=50,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': '3', })
    )
