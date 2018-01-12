from django.utils import timezone

from django.db import models
from django.db.models import QuerySet
from django.contrib.auth.models import User

'''
The Soft Delete functionaly code has bee copied from : https://medium.com/@adriennedomingus/soft-deletion-in-django-e4882581c340
It implements the Soft Delete, which means, it doesn't actually delete the object in real, just marks it as deleted
'''

class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)

class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()

class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class InsuranceCompany(SoftDeletionModel):
    name = models.CharField(max_length=50)
    logo = models.ImageField()  # incomplete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Customer(User):
    mobile = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VehicleMake(SoftDeletionModel):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VehicleModel(SoftDeletionModel):
    make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50)


class VehicleValue(SoftDeletionModel):
    make = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    value = models.FloatField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PolicyComprehensive(SoftDeletionModel):
    insuranceCompany = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    repairType = models.BooleanField()
    minVehicle = models.FloatField()
    maxVehicle = models.FloatField()
    premium = models.FloatField()
    minAmount = models.FloatField()
    commission = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PolicyTP(SoftDeletionModel):
    insuranceCompany = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    fixedValue = models.FloatField()
    minVehicle = models.FloatField()
    maxVehicle = models.FloatField()
    commission = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerPolicy(SoftDeletionModel):
    class Meta:
        abstract = True

    insuranceCompany = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    effectiveFrom = models.DateField(auto_now=False, auto_now_add=False)
    effectiveTill = models.DateField(auto_now=False, auto_now_add=False)
    year = models.IntegerField()
    value = models.FloatField()
    totalAmount = models.FloatField()
    commission = models.FloatField()
    policyType = models.BooleanField()
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomerPolicyComprehensive(CustomerPolicy):
    repairType = models.BooleanField()
    premium = models.FloatField()


class CustomerPolicyTP(CustomerPolicy):
    fixedValue = models.FloatField()