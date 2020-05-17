from django import forms

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    # (1)상세페이지에서 추가. False
    # (2)장바구니에서 수량 변경. True
