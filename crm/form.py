from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': "Имя"}))
    phone = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'input_text', 'placeholder': "Номер телефона"}))

    comment = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': "Комментарий",
                                                                           'style': 'height:150px'}))
