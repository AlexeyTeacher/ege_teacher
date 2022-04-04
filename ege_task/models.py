from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Способ решения')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Способ решения'
        verbose_name_plural = "Способы решений"


class Task(models.Model):
    number_task = models.CharField(max_length=10, default=28)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    preview_image = models.ImageField(upload_to="images/%Y/%m/%d")
    video_url = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.pk} >>> {self.title}"

    def get_absolute_url(self):
        return reverse('task', kwargs={'number_task': self.number_task})

    class Meta:
        verbose_name = 'Разбор задачи'
        verbose_name_plural = "Разборы задач"
        ordering = ['time_create', 'number_task']

