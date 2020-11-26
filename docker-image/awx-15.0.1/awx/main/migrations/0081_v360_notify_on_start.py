# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 20:35
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_split_unified_job_template_any(apps, schema_editor):
    UnifiedJobTemplate = apps.get_model('main', 'unifiedjobtemplate')
    for ujt in UnifiedJobTemplate.objects.all():
        for ujt_notification in ujt.notification_templates_any.all():
            ujt.notification_templates_success.add(ujt_notification)
            ujt.notification_templates_error.add(ujt_notification)

def forwards_split_organization_any(apps, schema_editor):
    Organization = apps.get_model('main', 'organization')
    for org in Organization.objects.all():
        for org_notification in org.notification_templates_any.all():
            org.notification_templates_success.add(org_notification)
            org.notification_templates_error.add(org_notification)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0080_v360_replace_job_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='notification_templates_started',
            field=models.ManyToManyField(blank=True, related_name='organization_notification_templates_for_started', to='main.NotificationTemplate'),
        ),
        migrations.AddField(
            model_name='unifiedjobtemplate',
            name='notification_templates_started',
            field=models.ManyToManyField(blank=True, related_name='unifiedjobtemplate_notification_templates_for_started', to='main.NotificationTemplate'),
        ),
        # Separate out "any" notifications into "success" and "error" before the "any" state gets deleted.
        migrations.RunPython(forwards_split_unified_job_template_any, None),
        migrations.RunPython(forwards_split_organization_any, None),
        migrations.RemoveField(
            model_name='organization',
            name='notification_templates_any',
        ),
        migrations.RemoveField(
            model_name='unifiedjobtemplate',
            name='notification_templates_any',
        ),
    ]
