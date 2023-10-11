from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Massage(models.Model):
    subject = models.CharField(max_length=100, verbose_name='тема')
    subject_body = models.TextField(verbose_name='содержание')

    def __str__(self):
        return f'self.subject'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
