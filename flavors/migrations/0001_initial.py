# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flavor'
        db.create_table(u'flavors_flavor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'flavors', ['Flavor'])


    def backwards(self, orm):
        # Deleting model 'Flavor'
        db.delete_table(u'flavors_flavor')


    models = {
        u'flavors.flavor': {
            'Meta': {'object_name': 'Flavor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['flavors']