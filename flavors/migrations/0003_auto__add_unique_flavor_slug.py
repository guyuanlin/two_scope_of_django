# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Flavor', fields ['slug']
        db.create_unique(u'flavors_flavor', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Flavor', fields ['slug']
        db.delete_unique(u'flavors_flavor', ['slug'])


    models = {
        u'flavors.flavor': {
            'Meta': {'object_name': 'Flavor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scoops_remaining': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['flavors']