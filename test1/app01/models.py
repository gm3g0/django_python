from django.db import models

##### 建造資料表 #####


class UserInfo(models.Model):  # 使用者
    email = models.CharField(verbose_name="信箱", max_length=100)
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密碼", max_length=64)
    sex = models.CharField(
        verbose_name="生理性別", max_length=4, null=True, blank=True)
    bithday = models.DateField(verbose_name="生日")
    Depart = models.ForeignKey(verbose_name="科系", to="Department",
                               to_field="id", null=True, blank=True, on_delete=models.SET_NULL)


class Department(models.Model):  # 科系別
    title = models.CharField(verbose_name="科系", max_length=32)

    def __str__(self):
        return self.title
