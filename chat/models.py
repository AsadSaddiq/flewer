# from django.contrib.auth.models import User
from django.db import models
from accounts.models import UserAccount



class Contact(models.Model):
    sender_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='send')
    receiver_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='rece')
    sender_name = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='sname')
    receiver_name = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='rname')
    img = models.CharField(max_length=120, null=True, blank=True)

    



class Message(models.Model):
    # contect=models.ForeignKey(Contact, on_delete=models.CASCADE)
    sender = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)