from django.db import models

# Create your models here.
## Model 상속
class Board(models.Model):
    title   = models.CharField(max_length=128, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    # fcuser 폴더에 있는  Fcuser 모델과 연결을 하겠다.
    writer  = models.ForeignKey('fcuser.Fcuser', on_delete= models.CASCADE, verbose_name="작성자")
    register_dttm = models.DateTimeField(auto_now_add= True, verbose_name="등록일")

    def __str__(self):
        return self.title

    class Meta():
        db_table = "Board"

        verbose_name = "게시글"
        verbose_name_plural = "게시글"
