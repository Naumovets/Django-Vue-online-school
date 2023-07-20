from django.db import models

from user.models import CustomUser


class Exam(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

    def __str__(self):
        return self.title


class Subject(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, related_name='subjects', verbose_name='Экзамен', null=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return str(self.exam) + ' ' + self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Course(models.Model):

    class Status(models.TextChoices):
        MAIN = 'MN', 'Основной'
        SPECIAL = 'SP', 'Спецкурс'
        FREE = 'FR', 'Бесплатный'

    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, related_name='courses', verbose_name='Предмет', null=True)
    title = models.CharField(max_length=150, verbose_name='Название')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.MAIN, verbose_name='Тип курса')
    image = models.ImageField(upload_to='courses/', verbose_name='Картинка', )
    description = models.TextField(verbose_name='Описание')
    chat = models.URLField(verbose_name='Беседа вк', blank=True, null=True)
    teacher = models.ForeignKey(CustomUser,
                                on_delete=models.SET_NULL,
                                related_name='teacher_courses',
                                verbose_name='Преподаватель',
                                null=True)
    price = models.DecimalField(verbose_name='Цена за месяц', decimal_places=0, max_digits=9, null=True, blank=True)
    full_price = models.DecimalField(verbose_name='Цена за курс до конца года', decimal_places=2, max_digits=9, null=True, blank=True)
    slug = models.SlugField(max_length=150)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return str(self.subject) + ' ' + self.title


class Webinar(models.Model):
    course = models.ForeignKey(Course,
                               on_delete=models.SET_NULL,
                               related_name='webinars',
                               verbose_name='Курс',
                               null=True)
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    code_of_translation = models.CharField(max_length=100, verbose_name='Код трансляции')
    date_start = models.DateTimeField(verbose_name='Дата начала')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Вебинар'
        verbose_name_plural = 'Вебинары'

    def __str__(self):
        return self.title


class Task(models.Model):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name='tasks', verbose_name='Вебинар')
    question = models.TextField(verbose_name='Условие текстом', blank=True, null=True)
    question_image = models.ImageField(upload_to='tasks/', verbose_name='Условие картинкой', blank=True, null=True)
    answer = models.TextField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return "Задача" + str(self.webinar) + " " + str(self.id)


class FileOfWebinar(models.Model):
    webinar = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name='files', verbose_name='Вебинар')
    file_of_webinar = models.FileField(upload_to='files/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Файл для вебинара'
        verbose_name_plural = 'Файлы для вебинаров'

    def __str__(self):
        return "Файл" + ' ' + str(self.webinar) + " " + str(self.id)


class Curator(models.Model):
    curator = models.ForeignKey(CustomUser,
                                on_delete=models.SET_NULL,
                                null=True,
                                verbose_name='Куратор',
                                related_name='curators')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='curators', verbose_name='Курс')

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'