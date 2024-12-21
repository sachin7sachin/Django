from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML","MASALA"),
        ("GR","GINGER"),
        ("K","KIWI"),
        ("PL","PLAIN"),
        ("EL","ELACHI")
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")


    def __str__(self):
        return self.name


#one to many

class chaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
    

#many to many

class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name
    
#one to one

class chaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"certificate for {self.name.chai}"
    

    
