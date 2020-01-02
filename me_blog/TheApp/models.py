from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, models.PROTECT)
# models.PROTECT is an on_delete value which protect the source model and if he is not existed or having a problem he raises an Error to alert us

    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='TheApp/profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    #כדי שרק משתמשים רשומים יוכלו ליצור פוסט
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True) #יכול להיות בלנק אם עוד לא פרסמתי ויכול להיות נול אם אני לא רוצה לציין תאריך פרסום

    def publish(self):
        self.published_date = timezone.now()
        self.save()
# נשתמש בפונקציה בעתיד כדי לתת ערך לתאריך הפרסום בעת פרסום הפוסט כשנלחץ על כפתור

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
        #בעתיד תהיה רשימת תגובות, ואם התגובה תהיה מאושרת ושווה לTrue אז נאשר אותה

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})
        #פונקציה שאחרי שניצור פוסט או תגובה תעביר אותנו לדף מסוים

    def __str__(self):
            return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete = models.PROTECT)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
        #פונקציה שאחרי שניצור פוסט או תגובה תעביר אותנו לדף מסוים

    def __str__(self):
        return self.text