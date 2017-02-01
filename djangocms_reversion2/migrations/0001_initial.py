# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('reversion', '0001_squashed_0004_auto_20160611_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(editable=False, unique=True, verbose_name='Content')),
            ],
            options={
                'verbose_name': 'HTML content',
                'verbose_name_plural': 'HTML contents',
            },
        ),
        migrations.CreateModel(
            name='PageMarker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(db_index=True, editable=False, max_length=15, verbose_name='language')),
                ('page', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='page_markers', to='cms.Page', verbose_name='page')),
            ],
        ),
        migrations.CreateModel(
            name='PageRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(db_index=True, editable=False, max_length=15, verbose_name='language')),
                ('page', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page', verbose_name='page')),
                ('revision', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='reversion.Revision', verbose_name='revision')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='PageRevisionPlaceholderContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_revision_placeholders', related_query_name='page_revision_placeholder', to='djangocms_reversion2.HtmlContent', verbose_name='HTML Content')),
                ('page_revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placeholder_contents', related_query_name='placeholder_content', to='djangocms_reversion2.PageRevision', verbose_name='Page revision')),
                ('placeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_revision_contents', related_query_name='page_revision_content', to='cms.Placeholder', verbose_name=b'Placeholder')),
            ],
            options={
                'verbose_name': 'Page revision placeholder content',
                'verbose_name_plural': 'Page revision placeholder contents',
            },
        ),
        migrations.AddField(
            model_name='pagemarker',
            name='page_revision',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='page_marker', to='djangocms_reversion2.PageRevision', verbose_name='page revision'),
        ),
        migrations.AlterUniqueTogether(
            name='pagerevisionplaceholdercontent',
            unique_together=set([('page_revision', 'placeholder')]),
        ),
        migrations.AlterUniqueTogether(
            name='pagerevision',
            unique_together=set([('language', 'page', 'revision')]),
        ),
        migrations.AlterUniqueTogether(
            name='pagemarker',
            unique_together=set([('language', 'page')]),
        ),
    ]
