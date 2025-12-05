from django import forms
from .models import Student

from .models import Student,Activity

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
        
class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields =('activity_date','status','note')
        widgets={
            'activity_date':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'note':forms.Textarea(attrs={'class':'form-control','rows':2}),
        }