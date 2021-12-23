# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Officeitems(models.Model):
	idoffice = models.AutoField(db_column='idOffice', primary_key=True, blank=True, null=False)  # Field name made lowercase.
	addresslocality = models.TextField(db_column='addressLocality', blank=True, null=True)  # Field name made lowercase.
	addressregion = models.TextField(db_column='addressRegion', blank=True, null=True)  # Field name made lowercase.
	postalcode = models.ForeignKey('Postalcodes', models.DO_NOTHING, db_column='postalCode', related_name='items')
	streetaddress = models.TextField(db_column='streetAddress', blank=True, null=True)  # Field name made lowercase.
	description = models.TextField(blank=True, null=True)
	name = models.TextField(blank=True, null=True)
	telephone = models.TextField(blank=True, null=True)
	openinghours = models.TextField(db_column='openingHours', blank=True, null=True)  # Field name made lowercase.
	latitude = models.TextField(blank=True, null=True)
	longitude = models.TextField(blank=True, null=True)
	url = models.TextField(blank=True, null=True)
	audtimestamp = models.TextField(db_column='audTimestamp', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'OfficeItems'


class Postalcodes(models.Model):
	idpostalcode = models.AutoField(db_column='idPostalCode', primary_key=True)  # Field name made lowercase.
	holidays = models.TextField(db_column="holidays")
	audtimestamp = models.TextField(db_column='audTimestamp', blank=True, null=True)  # Field name made lowercase.

	class Meta:
		managed = False
		db_table = 'PostalCodes'

	def __str__(self):
		return "{} : {}".format(self.idpostalcode,self.holidays)

