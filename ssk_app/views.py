from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #リダイレクト先を作るためにインポートする
from .models import Student
from .forms import StudentForm #作成したフォームをインポートする


  
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
    
     #生徒を新規登録のビュー
class StudentCreateView(CreateView):
    model = Student
    form_class =StudentForm
    template_name ='ssk_app/student_form.html' #新規も更新も同じテンプレートを使い回す
    success_url = reverse_lazy('student_list')#成功したら一覧ページへリダイレクト
    
    #生徒の更新ビュー
class StudentUpdateView(UpdateView):
    model = Student
    form_class =StudentForm
    template_name ='ssk_app/student_form.html' #新規も更新も同じテンプレートを使い回す
    success_url = reverse_lazy('student_list')#成功したら一覧ページへリダイレクト
    # <int:pk>で渡されたID顧客のデータを自動でフォームでセットしてくれる
    
    #顧客削除のビュー
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'ssk_app/student_confirm_delete.html'#削除確認用の専用テンプレート
    success_url = reverse_lazy('student_list')#成功したら一覧ページへリダイレクト