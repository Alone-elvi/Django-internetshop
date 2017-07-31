from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        try:
            return 'id - %s -> %s : %s' % (self.id, self.name, self.email)
        except:
            return '%s' % "Что то пошло не так."

    class Meta:
        verbose_name = "My subscriber"
        verbose_name_plural = "A lot of Subscribers"
