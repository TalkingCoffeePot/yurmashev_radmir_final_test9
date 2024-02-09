from django.db import models
from accounts.models import Profile

class PostModel(models.Model):
    image = models.ImageField('Картинка', upload_to='post_images')
    user = models.ForeignKey(Profile, verbose_name='Пользователь', related_name='usr_posts', on_delete=models.CASCADE)
    text = models.TextField('Текст публикации', max_length=1000)
    likes = models.ManyToManyField(Profile, related_name='user_likes', blank=True)
    date_add = models.DateField('Дата публикации', auto_now_add=True)
    

class CommentModel(models.Model):
    author = models.ForeignKey(Profile, verbose_name='Автор', related_name='a_comment', on_delete=models.SET_NULL, blank=True, null=True)
    post_model = models.ForeignKey(PostModel, verbose_name='Продукт', related_name='p_comment', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField('Текст отзыва', max_length=1500)
    date_add = models.DateField('Дата публикации', auto_now_add=True)
    date_edit = models.DateField('Дата редактирования', auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_author(self):
        return Profile.objects.get(username=self.author)
    
    def get_product(self):
        return Profile.objects.get(id=self.post_model)

