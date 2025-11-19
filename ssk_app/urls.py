from django.urls import path
from .views import StudentListView, StudentDetailView #作成したCBVをインポート

urlpatterns =[
    #生徒一覧ページ
    #path('', ...)はプロジェクトのurls.pyから引き継いだルートURLを指す
    path('', StudentListView.as_view(), name='student_list'),
    
    #生徒詳細ページ
    #<int:pk>はURLの一部(顧客ID)の変数として受け取るという意味
    #例:/student/1/ , /student/2/
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail')
    
]