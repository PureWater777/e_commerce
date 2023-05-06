from store.signals import order_created
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(order_created)
def on_order_created(sender, **kwargs):
    print(kwargs["order"])
