from django.db import models

# Create your models here.
class FSentence(models.Model):
    orig_text = models.CharField(max_length=200)
    sub_date = models.DateTimeField('date submitted')
    f_text = models.TextField()

    def __str__(self):
        return self.orig_text
