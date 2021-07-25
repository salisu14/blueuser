# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models




class User(AbstractUser):
    class Types(models.TextChoices):
        ACCOUNTANT = "Accountant",
	SALESPERSON = "Salesperson",
	STOREKEEPER = "Storekeeper"

 
     # Identify the type of user
    type = models.CharField(
	    _("Types"), 
	    max_length=50, 
	    choices=Types.choices,
	    default=Types.SALESPERSON
    )


    # Ensures that creating new users through proxy models works
    base_type = Types.SALESPERSON

    def save(self, *args, **kwargs):
	'''Add a default base_type when adding a new user '''
        if not self.pk:
            self.type = self.base_type
	return super().save(*args, **kwargs)


class AccountantManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)
        return query.filter(type=User.Types.ACCOUNTANT)

class SalespersonManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)
        return query.filter(type=User.Types.SALESPERSON)


class StorekeeperManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        query = super().get_queryset(*args, **kwargs)
        return query.filter(type=User.Types.STOREKEEPER)


class Accountant(User):
    # Sets the user type to Account 
    base_type = User.Types.ACCOUNTANT


    # Change the defaults manager to return only Accountants object
    objects = AccountantManager()


    # Prevents creating Accountant table in the database
    class Meta:
        proxy = True


class SalesPerson(User):
    # Sets the user type to Salesperson
    base_type = User.Types.SALESPERSON


    # Change the defaults manager to return only salesperson object
    objects = SalespersonManager()


    # Prevents creating salesperson  table in the database
    class Meta:
        proxy = True


class Storekeeper(User):
    # Sets the user type to Storekeeper
    base_type = User.Types.STOREKEEPER


    # Change the defaults manager to return only Storekeeper object
    objects = StorekeeperManager()


    # Prevents creating Storekeeper table in the database
    class Meta:
        proxy = True