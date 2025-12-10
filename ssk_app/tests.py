from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Student,Activity

# Create your tests here.
class StdentModelsTests(TestCase):
    """
    Studentモデルに関するテスト
    """
    
    def test_is_empty(self):
        """
        初期状態ではデータが〇件であること
        """
        saved_students = Student.objects.all()
        self.assertEqual(saved_students.count(),0)
        
    def test_create_student(self):
        """
        生徒データを一件制作し、正しく保存されるか
        """
        student = Student.objects.create(
            school_name="国立お試し学園",
            student_name="テスト・試し太郎",
            email="test@example.com",
            
        )
        
    #2 データーベースから全件取得
        saved_students = Student.objects.all()
    
    #3 検証(Assertion)
        self.assertEqual(saved_students.count(),1)
        self.assertEqual(saved_students[0].school_name, "国立お試し学園") 
    
class StudentViewTests(TestCase):
    """
    view(画面表示)に関するテスト
    """
        
    def setUp(self):
        """
        各メソッドの実行前に呼ばれる事前準備
        ユーザーを作成し、顧客データをも一件作っておく
        """
        #テスト用のユーザーを作成
        self.user= User.objects.create_user(username='testuser',password='password')
        #このユーザーが担当する生徒を作成
        self.student = Student.objects.create(
            school_name="自分の担当：大学附属県立テスティング学校",
            teacher_name="チャッキー・森口",
            email="a@example.com",
            user=self.user#重要：ユーザーに紐づける
        )
        #別のユーザーを作成(権限確認用)
        self.other_user = User.objects.create_user(username='otheruser',password='password')
            
    def test_login_required(self):
        """
        ログインしていない場合、ログインページにリダイレクトされるか？
        """
        #ログインせずに、一覧ページにアクセス
        response = self.client.get(reverse('student_list'))
            
        #302リダイレクト（ログインページへ飛ばす）
        self.assertEqual(response.status_code,302)
            
        #リダイレクト先がログインページであることを確認
        self.assertIn('/accounts/login/', response.url)
            
    def test_logged_in_users_can_see_list(self):
        """
        ログインユーザーは自分の担当生徒を見られるか？
        """
        #1,ログインする
        self.client.force_login(self.user)
            
        #2, 一覧ページへアクセス
        response = self.client.get(reverse('student_list'))
            
        #3,正常に表示される
        self.assertEqual(response.status_code,200)
            
        #4,画面に「自分の担当：大学附属県立テスティング学校」という文字が含まれているか検証
        self.assertContains(response, "自分の担当：大学附属県立テスティング学校")
        
    def test_cannot_see_others_data(self): # ★ 修正：他の test_... と同じインデント
        """
        別のユーザーでログインした場合、他人のデータは見えないはず
        """
        #1,別のユーザーでログイン
        self.client.force_login(self.other_user)
            
        #2,一覧ページにアクセス
        response = self.client.get(reverse('student_list'))
            
        #3,ページ自体は表示される(200)が
        self.assertEqual(response.status_code, 200)
            
        #4,他人の生徒データ(self.student)は表示されていないはず
        self.assertNotContains(response,"自分の担当：大学附属県立テスティング学校")