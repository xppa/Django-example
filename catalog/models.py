from django.db import models
from django.urls import reverse

class Doctor(models.Model):
    """Model representing an doctor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief about doctor", null=True)

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Client(models.Model):
    first_name = models.CharField(max_length=100, null=False, default='NewFirstName')
    last_name = models.CharField(max_length=100, null=True)
    date_of_bird = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11, null=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief about client")

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Event(models.Model):
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    note = models.CharField(max_length=200, null=True, help_text="Note about event")

    EVENT_STATUS = (
        ('d', 'Запланировано'),
        ('o', 'Успешно'),
        ('a', 'Отменено')
    )

    status = models.CharField(
        max_length=1,
        choices=EVENT_STATUS,
        blank=True,
        default='d',
        help_text='event status')

    EVENT_TYPE = (
        ('d', 'Очная консультация'),
        ('o', 'Удаленная консультация'),
        ('a', 'Самостоятельно')
    )

    type = models.CharField(
        max_length=1,
        choices=EVENT_TYPE,
        blank=True,
        default='o',
        help_text='event type')

    def __str__(self):
        """String for representing the Model object."""
        return '{0} - {1} - {2}'.format(self.client, self.doctor.last_name, self.time)

        return '{0} - {1} - {2} - {3}'.format(self.client.first_name, self.client.last_name, self.doctor.last_name, self.time)

