from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Tag(models.Model):
    name= models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name 


#生徒のクラス
class Student(models.Model):
    school_name = models.CharField(max_length=100, verbose_name="学校名")
    student_name = models.CharField(max_length=50, verbose_name="生徒名")
    teacher_name = models.CharField(max_length=50, verbose_name="担任教師名")
    email = models.EmailField(max_length=100,unique=True, verbose_name="メールアドレス")
    
    #学年
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True,verbose_name="担当者") 
    tags = models.ManyToManyField(Tag,blank=True,verbose_name="タグ")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新日時")
    def __str__(self):
        return self.student_name
 
#授業参加記録
class Activity(models.Model):
    #項目ステータス
    STATUS_CHOICES = (
        ('pending','未開始'),
        ('scheduled','参加予定'),
        ('attended','出席済み'),
        ('absent','欠席'),
        ('completed','完了'),
        
    )
#生徒が削除されたら関連する授業参加記録も削除する(CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="生徒名")
    activity_date = models.DateField(verbose_name="授業日")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending',verbose_name="進歩")
    note = models.TextField(max_length=100,verbose_name="特記事項")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    def __str__(self):
        return f"{self.student.student_name} - {self.get_status_display()}"
#レッスンのクラス    
#class Lesson(models.Model):
#    title = models.CharField(max_length=200, verbose_name="授業名")
#    date = models.DateField()
    
#登録のクラス
#class Enrollment(models.Model):
#    student = models.ForeignKey(Student, on_delete=models.CASCADE)
#    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
#    updated_at = models.DateTimeField(auto_now=True,verbose_name="更新日時")
    


