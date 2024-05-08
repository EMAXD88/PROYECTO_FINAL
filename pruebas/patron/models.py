# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Usuario')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    telephone = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')

    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # Verificar y agregar al grupo "empleado" si no está ya en él
        empleado_group, _ = Group.objects.get_or_create(name='empleado')
        if not instance.groups.filter(name='empleado').exists():
            instance.groups.add(empleado_group)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
