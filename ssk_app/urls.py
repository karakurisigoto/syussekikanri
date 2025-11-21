from django.urls import path
 #作成したCBVをインポート

from .views import(
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView
)

urlpatterns =[
    #生徒一覧ページ
    #path('', ...)はプロジェクトのurls.pyから引き継いだルートURLを指す
    path('', StudentListView.as_view(), name='student_list'),
    #path('student/<int:pk>/',StudentCreateView(), name='student_detail'),
    
    #生徒詳細ページ
    #<int:pk>はURLの一部(顧客ID)の変数として受け取るという意味
    #例:/student/1/ , /student/2/
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    
    #新規登録
    path('student/new/', StudentCreateView.as_view(), name='student_create'),
    
    #更新ページ
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_update'),
    
    #削除ページ
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
    
]