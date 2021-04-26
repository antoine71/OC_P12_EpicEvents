from django.db import models
from django.conf import settings
from django.db.models.deletion import SET_NULL


class Client(models.Model):
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    company_name = models.CharField(max_length=100)
    converted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.company_name}"


class Contract(models.Model):
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE, related_name='contracts')
    project_name = models.CharField(max_length=100)
    signed = models.BooleanField(default=False)
    amount = models.FloatField(null=True)
    payment_due_date = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return f"Contrat: {self.project_name}"


class Event(models.Model):
    contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='event')
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True)
    attendees = models.IntegerField(null=True)
    event_date = models.DateField(null=True)
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return f"Evènement: {self.contract.project_name}"
