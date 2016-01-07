# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

def upload_function(instance,filename):
    return 'documents/%s/%Y/%m/%d/%H/%M/%S' % (instance.user.username)

class Document(models.Model):
    docfile = models.FileField(upload_to=upload_function)
    user = models.ForeignKey(User, null=False, blank= False)
 #   sharedwith=models.ForeignKey()
#    uploaded_by = models.ForeignKey(User)
#    def get_my_files(self, current_user):
#        return self.objects.filter(uploaded_by=current_user)
class Person(models.Model):
    name=models.CharField(max_length=100,blank=False)
    to_user=models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='from_user',
        through = 'Event',
        through_fields=('from_user','to_user'),
        )

class Event(models.Model):
    shared_file=models.ForeignKey(Document)
    from_user=models.ForeignKey(Person,related_name='event_as_giver')
    to_user=models.ForeignKey(Person,related_name='event_as_received')


#    shared_by=models.ForeignKey(User,null=False,blank=False)
#class myuser(mo):
 #   f1=models.CharField();

