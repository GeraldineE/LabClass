from django.db import models

# Create your models here.
#nombre de clase primera letra mayuscula
class Curso(models.Model):
    datecreate = models.DateTimeField(auto_now_add=True)
    tittle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.tittle

class lesson (models.Model):
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle

