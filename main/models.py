from django.db.models import *

# Create your models here.
class Article(Model):
    name = TextField()
    info = TextField()
    image = TextField()
    date = DateField()

    class Meta:
        ordering = ["-date"]
