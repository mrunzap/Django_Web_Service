from django.db import models

# Create your models here.
## Model 상속
class Fcuser(models.Model):
    username = models.CharField(max_length=64, verbose_name="사용자 이름")
    useremail = models.EmailField(max_length =128, verbose_name="사용자 이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    register_dttm = models.DateTimeField(auto_now_add= True, verbose_name="등록일")

    def __str__(self):
        return self.username

    class Meta():
        db_table = "Fcuser"

        verbose_name = "관리자"
        verbose_name_plural = "관리자"
