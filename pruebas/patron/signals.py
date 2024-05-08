from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_trabajador_group(sender, instance, created, **kwargs):
    if created:
        try:
            trabajador = Group.objects.get(name='empleado')
        except Group.DoesNotExist:
            trabajador = Group.objects.create(name='empleado')
            trabajador = Group.objects.create(name='administrativo')
        instance.user.groups.add(trabajador)