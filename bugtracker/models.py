from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
class MyUser(AbstractUser):
    pass

class Ticket(models.Model):
    title = models.CharField(max_length=50)
    time_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    name_of_user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="name_of_user")
    NEW = "N"
    INPROGRESS = "P"
    DONE = "D"
    INVALID = "I"
    STATUS_OF_TICKET = [
        (NEW, 'New'),
        (INPROGRESS, "In Progress"),
        (DONE, 'Done'),
        (INVALID, "Invalid"),
    ]
    status_of_ticket = models.CharField(
        max_length=1,
        choices=STATUS_OF_TICKET,
        default=NEW,
    )
    
    user_assigned = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="user_assigned", blank=True, null=True)
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="completed_by", blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    