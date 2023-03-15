from django.db import models
from django.utils import timezone

# Create your models here.

class User (models.Model):
    username = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='Пользователь',db_column='Пользователь') # имя пользователя
    allow_admin = models.BooleanField(default=False,verbose_name='Права админа',db_column='Права админа') #права доступа
    
    def __str__(self) -> str:
        return f"{self.user_name}" # в админку возвращае имя пользователя
    
    class Meta:
        ordering = ["username"] # упорядочивается по имени
        verbose_name = 'Пользователя'  # отображение в админке если один пользователя
        verbose_name_plural = 'Пользователи'  # отображение в админке если два и более пользователя

class Video(models.Model):
    title = models.CharField(max_length=200,verbose_name='Название',db_column='Название')
    video = models.FileField(upload_to=f'video/viedos/',null=True,verbose_name='Видео',db_column='Видео')
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

class Image(models.Model):
    title = models.CharField(max_length=200,verbose_name='Название',db_column='Название')
    image = models.ImageField(upload_to=f'images/article',null=True,verbose_name='Изображение',db_column='Изображение')
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        ordering = ["title"]
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
    
class Article(models.Model): # класс статьи
    title = models.CharField(max_length=100,null=False,verbose_name='Название',db_column='Название') # название
    img = models.ManyToManyField(Image,verbose_name='Изображение',db_column='Изображение')  # изображения, которые учавствую в статьях наследуем от модели Image
    video = models.ManyToManyField(Video,verbose_name='Видео',db_column='Видео') # видео в статье наследуем от модели Video
    body = models.TextField(null=False,verbose_name='Текст',db_column='Текст') # текст статьи
    date = models.DateTimeField(default=timezone.now,verbose_name='Дата',db_column='Дата') # дата написания
    
    def __str__(self) -> str:
        return f"{self.title} - {self.date}" # в админку возвращаем название и дату
    
    class Meta:
        ordering = ["date"] # упорядочивается по дате в админке
        verbose_name = 'Статью' #  отображение в админкеесли одна статья
        verbose_name_plural = 'Статьи' # отображение в админкеесли две и более статьи
    
    
class Question(models.Model):
    question = models.TextField(verbose_name='Вопрос',db_column='Вопрос')
    answer = models.TextField(verbose_name='Ответ',db_column='Ответ')
    
    def __str__(self) -> str:
        return f"{self.question} - {self.answer}"
    
    class Meta:
        ordering = ["question"]
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
class ArticleQuestion(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='Пользователь',db_column='Пользователь')
    date = models.DateTimeField(default=timezone.now,verbose_name='Дата',db_column='Дата')
    text = models.TextField(verbose_name='Текст',db_column='Текст')
    article = models.ForeignKey(Article,on_delete=models.DO_NOTHING,verbose_name='Статья',db_column='Статья')
    
    def __str__(self) -> str:
        return f"{self.article} - {self.text}"
    
    class Meta:
        ordering = ["article"]
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
    


    

        
