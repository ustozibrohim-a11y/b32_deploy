from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class TeamMember(models.Model):
    f_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="teams/")

    facebook = models.URLField(max_length=255, null=True, blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)

    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name
