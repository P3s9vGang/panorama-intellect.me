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

class OfferedArticle(Model):
    name = TextField()
    info = TextField()
    image = TextField()
    date = DateField(auto_now_add = True)
    is_accepted = BooleanField()

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
