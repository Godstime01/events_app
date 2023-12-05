from collections.abc import Iterable
from django.db import models
from accounts.models import CustomUserModel
import uuid


class Event(models.Model):

    ONGOING = 'ongoing'
    COMPLETED = 'completed'
    UPCOMING = 'upcoming'

    STATUS = (
        (UPCOMING, 'Upcoming'),
        (ONGOING, 'Ongoing'),
        (COMPLETED, 'Completed')
    )

    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    max_participants = models.IntegerField(default=30)
    status = models.CharField(
        max_length=15, default='upcoming', choices=STATUS)
    organiser = models.ForeignKey(
        CustomUserModel, related_name='organiser', on_delete=models.CASCADE)

    def generate_invite_link(self):
        # return str(uuid.uuid4())[:10]
        return self.id

    def check_max_reached(self):
        return self.participationmodel_set.count() >= self.max_participants

    def get_participant_count(self):
        return self.participationmodel_set.count()

    def get_available_slot(self):
        if self.check_max_reached():
            return "No available slot"
        return self.max_participants - self.get_participant_count()


class ParticipationModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    location = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.event.check_max_reached():
            raise ValueError(
                "Cannot register for event, maximum participants reached.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
