from django.db import models

def img(instance, filename):
    return f"{instance.nome_img}-{filename}"

class Avatarheroes(models.Model):
    nome_img = models.CharField(primary_key=True, max_length=20)
    image =models.ImageField(upload_to=img, blank=True, null=True)
    



class Heroina(models.Model):
    nivel = models.IntegerField(db_column='Nivel', primary_key=True)  # Field name made lowercase.
    damage = models.IntegerField(db_column='Damage', blank=True, null=True)  # Field name made lowercase.
    hit = models.FloatField(db_column='Hit', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    upcost = models.IntegerField(db_column='UPcost', blank=True, null=True)  # Field name made lowercase.
    uptime = models.TextField(db_column='UPTime', blank=True, null=True)  # Field name made lowercase.
    th = models.IntegerField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Heroina'


class King(models.Model):
    nivel = models.IntegerField(db_column='Nivel', primary_key=True)  # Field name made lowercase.
    damage = models.IntegerField(db_column='Damage', blank=True, null=True)  # Field name made lowercase.
    hit = models.FloatField(db_column='Hit', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    upcost = models.IntegerField(db_column='UPcost', blank=True, null=True)  # Field name made lowercase.
    uptime = models.TextField(db_column='UPTime', blank=True, null=True)  # Field name made lowercase.
    th = models.IntegerField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'King'


class Quenn(models.Model):
    nivel = models.IntegerField(db_column='Nivel', primary_key=True)  # Field name made lowercase.
    damage = models.IntegerField(db_column='Damage', blank=True, null=True)  # Field name made lowercase.
    hit = models.FloatField(db_column='Hit', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    upcost = models.IntegerField(db_column='UPcost', blank=True, null=True)  # Field name made lowercase.
    uptime = models.TextField(db_column='UPTime', blank=True, null=True)  # Field name made lowercase.
    th = models.IntegerField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Quenn'


class Warden(models.Model):
    nivel = models.IntegerField(db_column='Nivel', primary_key=True)  # Field name made lowercase.
    damage = models.IntegerField(db_column='Damage', blank=True, null=True)  # Field name made lowercase.
    hit = models.FloatField(db_column='Hit', blank=True, null=True)  # Field name made lowercase.
    hp = models.FloatField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    aura = models.CharField(db_column='AURA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    upcost = models.IntegerField(db_column='UPcost', blank=True, null=True)  # Field name made lowercase.
    uptime = models.TextField(db_column='UPTime', blank=True, null=True)  # Field name made lowercase.
    th = models.IntegerField(db_column='TH', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Warden'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=100)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
