from django.db import models

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=15)  # 인물 이름
    detail = models.CharField(max_length=100)  # 명언
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title} - {self.created_at}'

    def get_absolute_url(self):
        return f'/today_word/{self.pk}/'