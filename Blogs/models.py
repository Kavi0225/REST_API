from django.db import models

class Blogss(models.Model):
    b_name = models.CharField(max_length=150)
    b_age = models.IntegerField()
    b_title = models.CharField(max_length=200)
    b_contant = models.ImageField(name=None)

    def __str__(self):
        return self.b_title  


class Comments(models.Model):
    blog = models.ForeignKey(Blogss, on_delete=models.CASCADE, related_name="comments")  
    name = models.CharField(max_length=150)
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.comment
