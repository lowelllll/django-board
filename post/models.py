# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class BoardTbl(models.Model):
    idx = models.AutoField(primary_key=True)
    writer = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board_tbl'


class CommentTbl(models.Model):
    idx = models.AutoField(primary_key=True)
    bidx = models.IntegerField(blank=True, null=True)
    writer = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_tbl'

