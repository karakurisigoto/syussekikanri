from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #リダイレクト先を作るためにインポートする
from .models import Student 
from .forms import StudentForm #作成したフォームをインポートする


#便利なお守りを入れるとログインが全てのviewでチェックされる。ログインしないと見れない書き換え防止
#1,LoginRequiredMixinをインポート
from django.contrib.auth.mixins import LoginRequiredMixin
#2,作成した全てのCBVにLoginRequiredMixinを追記（先に書くのが慣例）

# Create your views here.
#生徒一覧のページ用のビュー
class StudentListView(LoginRequiredMixin,ListView):
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
    #queryset=Student.objects.all().order_by('school_name')
    #このメソッドをオーバーライド(追記)
    def get_queryset(self):
        #ログインしているユーザー(self.request.user)が担当する
        #生徒のデータのみを学校名前順で取得する
        return Student.objects.filter(user=self.request.user).order_by('school_name')    
    
#生徒詳細用のページ
class StudentDetailView(LoginRequiredMixin,DetailView):
    """
    生徒の詳細を表示するビュー（DetailViewを継承）
    """
    #1.どのモデルのデータを取得するか？
    model = Student
    #2.どのテンプレートファイルを使うか？
    template_name = 'ssk_app/student_detail.html'
    #3.テンプレート内で使う変数（指定しない場合は'object'になるsつけない）
    context_object_name ='student'
    #このメソッドをオーバーライド(追記)
    def get_queryset(self):
    #自分が担当のデータのみを対象とする
        return Student.objects.filter(user=self.request.user)

     #生徒を新規登録のビュー
class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    form_class =StudentForm
    template_name ='ssk_app/student_form.html' #新規も更新も同じテンプレートを使い回す
    success_url = reverse_lazy('student_list')#成功したら一覧ページへリダイレクト

#このメソッドをオーバーライド（追記）
    def form_valid(self,form):
      #フォームが保存される直前に、担当者(user)フィールドに
      #現在ログインしているユーザー(self.request.user)をセットする
      form.instance.user = self.request.user
      #親クラス(CreateView)のform_validを呼び出し、保存処理を続行
      return super().form_valid(form)

    #生徒の更新ビュー
class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    form_class =StudentForm
    template_name ='ssk_app/student_form.html' #新規も更新も同じテンプレートを使い回す
    success_url = reverse_lazy('student_list')#成功したら一覧ページへリダイレクト
    # <int:pk>で渡されたID顧客のデータを自動でフォームでセットしてくれる
        #このメソッドをオーバーライド(追記)
    def get_queryset(self):
    #自分が担当のデータのみを対象とする
        return Student.objects.filter(user=self.request.user)

    #顧客削除のビュー
class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    template_name = 'ssk_app/student_confirm_delete.html'#削除確認用の専用テンプレート
    success_url = reverse_lazy('student_list')#成功したら一覧ページへリダイレクト
        #このメソッドをオーバーライド(追記)
    def get_queryset(self):
    #自分が担当のデータのみを対象とする
        return Student.objects.filter(user=self.request.user)
