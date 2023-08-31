from enum import Enum
from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from EcommerceProject.Core.model_mixins import ChoicesEnumMixin
from EcommerceProject.Core.validators import validate_only_letters


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30
    MAX_LENGTH_LOCALITY = 200
    MAX_LENGTH_CITY = 200

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    locality = models.CharField(
        max_length=MAX_LENGTH_LOCALITY,
        validators=(
            validate_only_letters,
        )
    )

    city = models.CharField(
        max_length=MAX_LENGTH_CITY,
        validators=(
            validate_only_letters,
        )
    )

    mobile = models.IntegerField(
        default=0
    )

    zipcode = models.IntegerField(
        null=True,
        blank=True,
    )
