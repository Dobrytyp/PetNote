from django.db import models
from django.shortcuts import reverse

# Create your models here.


class GCalEntry(models.Model):

    title = models.CharField(max_length=100)
    start_event = models.DateTimeField()
    end_event = models.DateTimeField()
    all_day = models.BooleanField(
        choices=[
            ('No', 'Not all day'),
            ('Yes', 'All day')
        ]
    )
    repeat_event = models.CharField(
        max_length=10,
        choices=[
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
            ('yearly', 'Every year')
        ]
    )
    notification = models.CharField(
        max_length=100,
        choices=[
            ('email', 'Email'),
            ('notification', 'Notificaton'),
            ('none', 'None')
        ]
    )
    state = models.CharField(
        max_length=100,
        choices=[
            ('busy', 'Busy'),
            ('free', 'Free')
        ]
    )
    privacy = models.CharField(
        max_length=100,
        choices=[
            ('private', 'Private'),
            ('public', 'Public')
        ]
    )
    active = models.BooleanField(
        max_length=50,
        choices=[
            ('active', 'Active'),
            ('not_active', 'Not active')
        ]
    )

    def __str__(self):
        return f'{self.title}, {self.start_event}, {self.end_event}\
            {self.all_day}, {self.repeat_event}, {self.notification}\
            {self.state}, {self.privacy}, {self.active}'

    def get_absolute_url(self):
        return reverse('gcal:event-list')
