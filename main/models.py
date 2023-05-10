from django.db import models


def get_default_translation_json():
    return {"en": ""}


class MasterDatapoint(models.Model):
    name = models.CharField(max_length=100, unique=True)
    definition = models.JSONField(default=get_default_translation_json)
