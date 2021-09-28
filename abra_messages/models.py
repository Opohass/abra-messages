from django.db import models
from django.contrib.auth.models import User


class AbraMessages(models.Model):
    """ AbraMessage is a model containing sender, receiver"""
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    subject = models.CharField(max_length=256)
    creation_date = models.DateTimeField(auto_now_add=True)
    msg_read = models.BooleanField(default=False)

    def __str__(self):
        return '%s:\n%s' % (self.subject, self.message)