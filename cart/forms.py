from django import forms
# 폼을 쓰는 이유1 : 클라이언트 화면에 입력 폼을 만들어주려고
# 폼을 쓰는 이유2 : 클라이언트가 입력한 데이터에 대한 전처리

class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput) # BooleanField에서는 required=False로 해놔야 해.
    # widget=forms.HiddenInput 사용자에게 노출될 때 뭘 쓸건데? 사용자가 보고 고르는 값이 아니라서 hidden으로 넣어주는 것임.