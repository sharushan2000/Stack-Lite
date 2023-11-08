from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name="profile") 
    is_email_activated  = models.BooleanField(default=False)
    bio = models.TextField(max_length=500 , blank=True ,default="---")
    pic = models.ImageField(default="default.jbg", upload_to="profile_pics")
    public = models.BooleanField(default=False)
    github = models.URLField(blank=True)


    def __str__(self) -> str:
        return self.user.first_name + " " + self.user.username
    



class Ticket(models.Model):
    title = models.CharField(max_length=200)
    describe = models.TextField(max_length=500)
    code = models.TextField(blank=True)
    maker = models.ForeignKey(User , on_delete=models.CASCADE,related_name="tickets")
    created_date= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self) -> str:
        return self.title




class Comment(models.Model):
    title = models.CharField(max_length=200)
    solution = models.TextField(max_length=500)
    code = models.TextField(max_length=500 , blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    solution_for = models.ForeignKey(Ticket , on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self) -> str:
        return self.user.username +" : "  + self.title
    


    

