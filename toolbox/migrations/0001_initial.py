# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'License'
        db.create_table(u'toolbox_license', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('license_md', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('license_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('open_source', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('toolbox', ['License'])

        # Adding model 'Property'
        db.create_table(u'toolbox_property', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('intro', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('is_good', self.gf('django.db.models.fields.BooleanField')()),
            ('is_bad', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal('toolbox', ['Property'])

        # Adding model 'Tool'
        db.create_table(u'toolbox_tool', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('intro_md', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('intro_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_md', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('credit', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tool_image', null=True, to=orm['filer.Image'])),
            ('feature_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('published', self.gf('django.db.models.fields.BooleanField')()),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('author_url', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('license', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['toolbox.License'], blank=True)),
            ('risk', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('playstore', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('appstore', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('marketplace', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
        ))
        db.send_create_signal('toolbox', ['Tool'])

        # Adding M2M table for field platforms on 'Tool'
        m2m_table_name = db.shorten_name(u'toolbox_tool_platforms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tool', models.ForeignKey(orm['toolbox.tool'], null=False)),
            ('platform', models.ForeignKey(orm['toolbox.platform'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tool_id', 'platform_id'])

        # Adding M2M table for field formfactors on 'Tool'
        m2m_table_name = db.shorten_name(u'toolbox_tool_formfactors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tool', models.ForeignKey(orm['toolbox.tool'], null=False)),
            ('formfactor', models.ForeignKey(orm['toolbox.formfactor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tool_id', 'formfactor_id'])

        # Adding M2M table for field categories on 'Tool'
        m2m_table_name = db.shorten_name(u'toolbox_tool_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tool', models.ForeignKey(orm['toolbox.tool'], null=False)),
            ('category', models.ForeignKey(orm['toolbox.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tool_id', 'category_id'])

        # Adding M2M table for field pros on 'Tool'
        m2m_table_name = db.shorten_name(u'toolbox_tool_pros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tool', models.ForeignKey(orm['toolbox.tool'], null=False)),
            ('property', models.ForeignKey(orm['toolbox.property'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tool_id', 'property_id'])

        # Adding M2M table for field cons on 'Tool'
        m2m_table_name = db.shorten_name(u'toolbox_tool_cons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tool', models.ForeignKey(orm['toolbox.tool'], null=False)),
            ('property', models.ForeignKey(orm['toolbox.property'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tool_id', 'property_id'])

        # Adding M2M table for field alternative on 'Tool'
        m2m_table_name = db.shorten_name(u'toolbox_tool_alternative')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_tool', models.ForeignKey(orm['toolbox.tool'], null=False)),
            ('to_tool', models.ForeignKey(orm['toolbox.tool'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_tool_id', 'to_tool_id'])

        # Adding model 'Service'
        db.create_table(u'toolbox_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('intro_md', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('intro_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_md', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('credit', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='service_image', null=True, to=orm['filer.Image'])),
            ('feature_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('published', self.gf('django.db.models.fields.BooleanField')()),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('author_url', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('license', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['toolbox.License'], blank=True)),
            ('risk', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('toolbox', ['Service'])

        # Adding M2M table for field platforms on 'Service'
        m2m_table_name = db.shorten_name(u'toolbox_service_platforms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm['toolbox.service'], null=False)),
            ('platform', models.ForeignKey(orm['toolbox.platform'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'platform_id'])

        # Adding M2M table for field formfactors on 'Service'
        m2m_table_name = db.shorten_name(u'toolbox_service_formfactors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm['toolbox.service'], null=False)),
            ('formfactor', models.ForeignKey(orm['toolbox.formfactor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'formfactor_id'])

        # Adding M2M table for field categories on 'Service'
        m2m_table_name = db.shorten_name(u'toolbox_service_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm['toolbox.service'], null=False)),
            ('category', models.ForeignKey(orm['toolbox.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'category_id'])

        # Adding M2M table for field pros on 'Service'
        m2m_table_name = db.shorten_name(u'toolbox_service_pros')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm['toolbox.service'], null=False)),
            ('property', models.ForeignKey(orm['toolbox.property'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'property_id'])

        # Adding M2M table for field cons on 'Service'
        m2m_table_name = db.shorten_name(u'toolbox_service_cons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm['toolbox.service'], null=False)),
            ('property', models.ForeignKey(orm['toolbox.property'], null=False))
        ))
        db.create_unique(m2m_table_name, ['service_id', 'property_id'])

        # Adding M2M table for field alternative on 'Service'
        m2m_table_name = db.shorten_name(u'toolbox_service_alternative')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_service', models.ForeignKey(orm['toolbox.service'], null=False)),
            ('to_service', models.ForeignKey(orm['toolbox.service'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_service_id', 'to_service_id'])

        # Adding model 'Advice'
        db.create_table(u'toolbox_advice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('intro_md', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('intro_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_md', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_html', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('credit', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='advice_image', null=True, to=orm['filer.Image'])),
            ('feature_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('published', self.gf('django.db.models.fields.BooleanField')()),
            ('time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('toolbox', ['Advice'])

        # Adding M2M table for field platforms on 'Advice'
        m2m_table_name = db.shorten_name(u'toolbox_advice_platforms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advice', models.ForeignKey(orm['toolbox.advice'], null=False)),
            ('platform', models.ForeignKey(orm['toolbox.platform'], null=False))
        ))
        db.create_unique(m2m_table_name, ['advice_id', 'platform_id'])

        # Adding M2M table for field formfactors on 'Advice'
        m2m_table_name = db.shorten_name(u'toolbox_advice_formfactors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advice', models.ForeignKey(orm['toolbox.advice'], null=False)),
            ('formfactor', models.ForeignKey(orm['toolbox.formfactor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['advice_id', 'formfactor_id'])

        # Adding M2M table for field categories on 'Advice'
        m2m_table_name = db.shorten_name(u'toolbox_advice_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('advice', models.ForeignKey(orm['toolbox.advice'], null=False)),
            ('category', models.ForeignKey(orm['toolbox.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['advice_id', 'category_id'])

        # Adding M2M table for field related on 'Advice'
        m2m_table_name = db.shorten_name(u'toolbox_advice_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_advice', models.ForeignKey(orm['toolbox.advice'], null=False)),
            ('to_advice', models.ForeignKey(orm['toolbox.advice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_advice_id', 'to_advice_id'])

        # Adding model 'ParentCategories'
        db.create_table(u'toolbox_parentcategories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('show_in_nav', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('toolbox', ['ParentCategories'])

        # Adding M2M table for field categories on 'ParentCategories'
        m2m_table_name = db.shorten_name(u'toolbox_parentcategories_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('parentcategories', models.ForeignKey(orm['toolbox.parentcategories'], null=False)),
            ('category', models.ForeignKey(orm['toolbox.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['parentcategories_id', 'category_id'])

        # Adding model 'Formfactor'
        db.create_table(u'toolbox_formfactor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('show_in_nav', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('toolbox', ['Formfactor'])

        # Adding M2M table for field platforms on 'Formfactor'
        m2m_table_name = db.shorten_name(u'toolbox_formfactor_platforms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('formfactor', models.ForeignKey(orm['toolbox.formfactor'], null=False)),
            ('platform', models.ForeignKey(orm['toolbox.platform'], null=False))
        ))
        db.create_unique(m2m_table_name, ['formfactor_id', 'platform_id'])

        # Adding model 'Category'
        db.create_table(u'toolbox_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('show_in_nav', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_in_sitemap', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('toolbox', ['Category'])

        # Adding model 'Platform'
        db.create_table(u'toolbox_platform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal('toolbox', ['Platform'])

        # Adding model 'MainNav'
        db.create_table(u'toolbox_mainnav', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('toolbox', ['MainNav'])

        # Adding M2M table for field categories on 'MainNav'
        m2m_table_name = db.shorten_name(u'toolbox_mainnav_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mainnav', models.ForeignKey(orm['toolbox.mainnav'], null=False)),
            ('parentcategories', models.ForeignKey(orm['toolbox.parentcategories'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mainnav_id', 'parentcategories_id'])


    def backwards(self, orm):
        # Deleting model 'License'
        db.delete_table(u'toolbox_license')

        # Deleting model 'Property'
        db.delete_table(u'toolbox_property')

        # Deleting model 'Tool'
        db.delete_table(u'toolbox_tool')

        # Removing M2M table for field platforms on 'Tool'
        db.delete_table(db.shorten_name(u'toolbox_tool_platforms'))

        # Removing M2M table for field formfactors on 'Tool'
        db.delete_table(db.shorten_name(u'toolbox_tool_formfactors'))

        # Removing M2M table for field categories on 'Tool'
        db.delete_table(db.shorten_name(u'toolbox_tool_categories'))

        # Removing M2M table for field pros on 'Tool'
        db.delete_table(db.shorten_name(u'toolbox_tool_pros'))

        # Removing M2M table for field cons on 'Tool'
        db.delete_table(db.shorten_name(u'toolbox_tool_cons'))

        # Removing M2M table for field alternative on 'Tool'
        db.delete_table(db.shorten_name(u'toolbox_tool_alternative'))

        # Deleting model 'Service'
        db.delete_table(u'toolbox_service')

        # Removing M2M table for field platforms on 'Service'
        db.delete_table(db.shorten_name(u'toolbox_service_platforms'))

        # Removing M2M table for field formfactors on 'Service'
        db.delete_table(db.shorten_name(u'toolbox_service_formfactors'))

        # Removing M2M table for field categories on 'Service'
        db.delete_table(db.shorten_name(u'toolbox_service_categories'))

        # Removing M2M table for field pros on 'Service'
        db.delete_table(db.shorten_name(u'toolbox_service_pros'))

        # Removing M2M table for field cons on 'Service'
        db.delete_table(db.shorten_name(u'toolbox_service_cons'))

        # Removing M2M table for field alternative on 'Service'
        db.delete_table(db.shorten_name(u'toolbox_service_alternative'))

        # Deleting model 'Advice'
        db.delete_table(u'toolbox_advice')

        # Removing M2M table for field platforms on 'Advice'
        db.delete_table(db.shorten_name(u'toolbox_advice_platforms'))

        # Removing M2M table for field formfactors on 'Advice'
        db.delete_table(db.shorten_name(u'toolbox_advice_formfactors'))

        # Removing M2M table for field categories on 'Advice'
        db.delete_table(db.shorten_name(u'toolbox_advice_categories'))

        # Removing M2M table for field related on 'Advice'
        db.delete_table(db.shorten_name(u'toolbox_advice_related'))

        # Deleting model 'ParentCategories'
        db.delete_table(u'toolbox_parentcategories')

        # Removing M2M table for field categories on 'ParentCategories'
        db.delete_table(db.shorten_name(u'toolbox_parentcategories_categories'))

        # Deleting model 'Formfactor'
        db.delete_table(u'toolbox_formfactor')

        # Removing M2M table for field platforms on 'Formfactor'
        db.delete_table(db.shorten_name(u'toolbox_formfactor_platforms'))

        # Deleting model 'Category'
        db.delete_table(u'toolbox_category')

        # Deleting model 'Platform'
        db.delete_table(u'toolbox_platform')

        # Deleting model 'MainNav'
        db.delete_table(u'toolbox_mainnav')

        # Removing M2M table for field categories on 'MainNav'
        db.delete_table(db.shorten_name(u'toolbox_mainnav_categories'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        'toolbox.advice': {
            'Meta': {'object_name': 'Advice'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'content_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_md': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feature_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'formfactors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Formfactor']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'advice_image'", 'null': 'True', 'to': "orm['filer.Image']"}),
            'intro_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'intro_md': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Platform']", 'symmetrical': 'False', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_rel_+'", 'blank': 'True', 'to': "orm['toolbox.Advice']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'toolbox.category': {
            'Meta': {'object_name': 'Category'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'show_in_nav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'toolbox.formfactor': {
            'Meta': {'object_name': 'Formfactor'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Platform']", 'symmetrical': 'False', 'blank': 'True'}),
            'show_in_nav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'toolbox.license': {
            'Meta': {'object_name': 'License'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'license_md': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'open_source': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'toolbox.mainnav': {
            'Meta': {'object_name': 'MainNav'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.ParentCategories']", 'symmetrical': 'False', 'blank': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'toolbox.parentcategories': {
            'Meta': {'object_name': 'ParentCategories'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'show_in_nav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'toolbox.platform': {
            'Meta': {'object_name': 'Platform'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'toolbox.property': {
            'Meta': {'object_name': 'Property'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_bad': ('django.db.models.fields.BooleanField', [], {}),
            'is_good': ('django.db.models.fields.BooleanField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'toolbox.service': {
            'Meta': {'object_name': 'Service'},
            'alternative': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'alternative_rel_+'", 'blank': 'True', 'to': "orm['toolbox.Service']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'author_url': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'cons': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'service_cons'", 'blank': 'True', 'to': "orm['toolbox.Property']"}),
            'content_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_md': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feature_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'formfactors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Formfactor']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'service_image'", 'null': 'True', 'to': "orm['filer.Image']"}),
            'intro_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'intro_md': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'license': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['toolbox.License']", 'blank': 'True'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Platform']", 'symmetrical': 'False', 'blank': 'True'}),
            'pros': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'service_pros'", 'blank': 'True', 'to': "orm['toolbox.Property']"}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
            'risk': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        'toolbox.tool': {
            'Meta': {'object_name': 'Tool'},
            'alternative': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'alternative_rel_+'", 'blank': 'True', 'to': "orm['toolbox.Tool']"}),
            'appstore': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'author_url': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'cons': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'tool_cons'", 'blank': 'True', 'to': "orm['toolbox.Property']"}),
            'content_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_md': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'feature_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'formfactors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Formfactor']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tool_image'", 'null': 'True', 'to': "orm['filer.Image']"}),
            'intro_html': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'intro_md': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'license': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['toolbox.License']", 'blank': 'True'}),
            'marketplace': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['toolbox.Platform']", 'symmetrical': 'False', 'blank': 'True'}),
            'playstore': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'pros': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'tool_pros'", 'blank': 'True', 'to': "orm['toolbox.Property']"}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
            'risk': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['toolbox']