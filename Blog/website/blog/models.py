from django.db import models
from django import forms

class Tag(models.Model):
    tag = models.CharField(max_length=64)
    #post = models.ForeignKey()

    def __str__(self):
        return self.tag

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=240)
    content = models.TextField()
    author = models.CharField(max_length=128, default="")
    #tags = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True, related_name='tags')
    # tags = forms.ModelMultipleChoiceField(queryset = Tag.objects.all())
    tags = models.ManyToManyField(Tag)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title