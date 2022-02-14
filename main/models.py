from django.db.models import *

# Create your models here.
class Article(Model):
    name = TextField(verbose_name = "Заголовок")
    info = TextField(verbose_name = "Информация")
    image = TextField(verbose_name = "Картинка")
    date = DateField(auto_now_add = True, verbose_name = "Дата")

    class Meta:
        ordering = ["-date"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class OfferedArticle(Model):
    name = TextField(verbose_name = "Заголовок")
    info = TextField(verbose_name = "Информация")
    image = TextField(verbose_name = "Картинка")
    date = DateField(auto_now_add = True, verbose_name = "Дата")
    is_accepted = BooleanField(verbose_name = "Опубликовано?")

    def save(self, *args, **kwargs):
        if self.is_accepted:
            Article(name = self.name, info = self.info, image = self.image, date = self.date).save()
            self.delete()
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.

    class Meta:
        ordering = ["-date"]
        verbose_name = "Предложенная новость"
        verbose_name_plural = "Предложенные новости"
