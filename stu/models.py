# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()


class LoginUser(models.Model):
    name = models.CharField(max_length=55)
    pwd = models.CharField(max_length=55)

    class Meta:
        db_table = 'login_user'


class PagingClazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=15)


class PagingCourse(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=55)


class PagingPcard(models.Model):
    person = models.ForeignKey('PagingPerson', primary_key=True)
    address = models.CharField(max_length=55)


class PagingPerson(models.Model):
    pno = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=5)


class PagingStudent(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=5)
    cno = models.ForeignKey(PagingClazz)


class PagingTeacher(models.Model):
    tno = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=55)


class PagingTeacherCour(models.Model):
    teacher = models.ForeignKey(PagingTeacher)
    course = models.ForeignKey(PagingCourse)
