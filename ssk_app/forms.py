from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student #どのモデルをベースにするか？
        
        #フォームに表示するフィールド
        fields =('school_name','student_name','email','user','tags')
        
        #必須項目したくない場合は以下を書き込む
        #今回はuser,tagsを必須にしない
        widgets={
            'user':forms.Select(attrs={'class': 'form-contarol'}),
            'tags':forms.SelectMultiple(attrs={'class': 'form-control'}),
        }