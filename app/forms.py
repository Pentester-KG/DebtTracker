from django import forms
from debt_backend.app import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Debt
        fields = '__all__'


    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Сумма должна быть положительным числом.")
        return amount

    def clean_debtor_name(self):
        debtor_name = self.cleaned_data.get('debtor_name')
        if not debtor_name:
            raise forms.ValidationError("Имя должника не может быть пустым.")
        return debtor_name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description) > 500:
            raise forms.ValidationError("Описание не должно превышать 500 символов.")
        return description

