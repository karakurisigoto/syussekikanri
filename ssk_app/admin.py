from django.contrib import admin
from .models import Student, Activity, Tag

#admin.site.register(Student)
#admin.site.register(Activity)
#admin.site.register(Tag)
# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('id','name')
    search_fields=('name',)
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #画面に出す、models.pyに書いてある
    list_display =('school_name','student_name','teacher_name','email','user','created_at')
    #絞り込み
    list_filter=('school_name','student_name','email')
    #検索機能
    search_fields =('school_name','student_name','email')
    #編集画面でのレイアウトここで'teacher_name',抜けるとadminで入力できないぞ！
    fieldsets = (
        ('基本情報',{'fields':('school_name','student_name','teacher_name','email')}),
        ('担当・タグ',{'fields':('user','tags')}),
    )   
    #多対多（tags)を編集しやすくする
    fields_horizontal=('tags',)
    #編集画面で児童入力される項目を読み取り専用に
    readonly_fields =('created_at','updated_at')
#Activityモデルの設定
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display=('student','activity_date','status','created_at')
    list_filter=('status','activity_date','student__user')#授業内容で絞り込める
    search_fields=('student__student_name','note')#生徒名や特記事項で検索
    #日付での絞り込みを便利にする
    date_hierarchy='activity_date'
    #編集画面での項目
    fields=('student','activity_date','status','note')
    #生徒の選択を検索ボックスにして表示を高速化（raw_id_fields)
    raw_id_fields=('student',)