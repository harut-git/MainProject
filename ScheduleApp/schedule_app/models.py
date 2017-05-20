from __future__ import unicode_literals

from django.db import models


# Create your models here.
#
class Lecturer(models.Model):
    name = models.CharField(max_length=200)
    classroom = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Weekday(models.Model):
    day_name = models.CharField(max_length=200)
    lecturer = models.ManyToManyField(Lecturer)

    def __str__(self):
        return self.day_name
        #

        #
        #         # john = Lecturers(name="John Williams", classroom="number 3")
        #         # monday = Weekdays(day_name="Monday", lect_name=john.name, lect_room=john.classroom)
        #         # john.save()
        #         # monday.save()
        #
        #
# smith = Lecturer(name='Sarah', classroom='202', id=2)
# smith.save()
# monday = Weekday(day_name="Monday", lecturer=smith)
# monday.save()
