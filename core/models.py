from django.db import models
from stdimage.models import StdImageField
# Create your models here.
'''
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Serico(Base):
    ICONE_CHOICES = {
        ('lni-cog', 'Engrenagem'),
        ()
    }
    '''