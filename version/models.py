from django.db.models import Model, CharField


class Version(Model):
    version = CharField(verbose_name='Версия', max_length=25)
