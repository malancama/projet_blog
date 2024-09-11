from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(_("Category"), max_length=130)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(_("Titre"), max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sumary = models.CharField(_("Sommaire"), max_length=50, null=True)
    content = models.TextField(_("contenu"))
    image = models.ImageField(_("images"), upload_to='images')
    date_pub=models.DateField(_("Date de publication"), null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return self.title



class Comment(models.Model):
    content = models.TextField(_("contenu"))
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        return f"{self.created_at}"