from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Student

  
# Create your views here.
#生徒一覧のページ用のビュー
class StudentListView(ListView):
    """
    生徒一覧を表示するビュー(ListViewを継承)
    """
    #1.どのモデルのデータを取得するか？
    model = Student
    #2.どのテンプレートファイルを使うか？
    template_name = 'ssk_app/student_list.html'
    #3.テンプレート内で使う変数（指定しない場合は'object_list'になるsつけといた）
    context_object_name ='students'
    #4.おまけ：１ページに表示する件数
    paginate_by = 10
    #5.おまけ：並びの指定（学校名）
    queryset=Student.objects.all().order_by('school_name')
    
#生徒詳細用のページ
class StudentDetailView(DetailView):
    """
    生徒の詳細を表示するビュー（DetailViewを継承）
    """
    #1.どのモデルのデータを取得するか？
    model = Student
    #2.どのテンプレートファイルを使うか？
    template_name = 'ssk_app/student_detail.html'
    #3.テンプレート内で使う変数（指定しない場合は'object'になるsつけない）
    context_object_name ='student'