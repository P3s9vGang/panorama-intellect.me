from django.db.models import *

# Create your models here.
class Article(Model):
    name = TextField()
    info = TextField()
    image = TextField()
    date = DateField(auto_now_add = True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


    def __str__(self):
        return '"{:<150}" от {}'.format(self.name, self.date)
