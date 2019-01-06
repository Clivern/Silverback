# Generated by Django 2.1.2 on 2019-01-06 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField(verbose_name='Activity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Related user'
                )),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('uptime', models.CharField(choices=[
                    ('on', 'ON'),
                    ('off', 'OFF')
                ], default='off', max_length=50, verbose_name='Uptime')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Component_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('uri', models.CharField(max_length=50, unique=True, verbose_name='URI')),
                ('status', models.CharField(choices=[
                    ('open', 'OPEN'),
                    ('closed', 'CLOSED')
                ], default='open', max_length=50, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Incident_Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[
                    ('Investigating', 'INVESTIGATING'),
                    ('Identified', 'IDENTIFIED'),
                    ('Monitoring', 'MONITORING'),
                    ('Update', 'UPDATE'),
                    ('Resolved', 'RESOLVED')
                ], default='open', max_length=50, verbose_name='Status')),
                ('notify_subscribers', models.CharField(choices=[
                    ('on', 'ON'),
                    ('off', 'OFF')
                ], default='on', max_length=50, verbose_name='Notify Subscribers')),
                ('datetime', models.DateTimeField(verbose_name='Datetime')),
                ('message', models.TextField(verbose_name='Message')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('incident', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='app.Incident',
                    verbose_name='Related Incident'
                )),
            ],
        ),
        migrations.CreateModel(
            name='Incident_Update_Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[
                    ('operational', 'OPERATIONAL'),
                    ('degraded_performance', 'DEGRADED_PERFORMANCE'),
                    ('partial_outage', 'PARTIAL_OUTAGE'),
                    ('major_outage', 'MAJOR_OUTAGE'),
                    ('maintenance', 'MAINTENANCE')
                ], default='operational', max_length=50, verbose_name='Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('component', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='app.Component',
                    verbose_name='Related Component'
                )),
                ('incident_update', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='app.Incident_Update',
                    verbose_name='Related Incident Update'
                )),
            ],
        ),
        migrations.CreateModel(
            name='Incident_Update_Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[
                    ('pending', 'PENDING'),
                    ('failed', 'FAILED'),
                    ('success', 'SUCCESS')
                ], default='pending', max_length=50, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('incident_update', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='app.Incident_Update',
                    verbose_name='Related Incident Update'
                )),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('type', models.CharField(choices=[
                    ('graphite', 'GRAPHITE'),
                    ('prometheus', 'PROMETHEUS')
                ], default='graphite', max_length=50, verbose_name='Type')),
                ('source', models.TextField(verbose_name='Source')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight', models.CharField(max_length=200, verbose_name='Highlight')),
                ('notification', models.CharField(max_length=200, verbose_name='Notification')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('type', models.CharField(choices=[
                    ('pending', 'PENDING'),
                    ('failed', 'FAILED'),
                    ('passed', 'PASSED'),
                    ('error', 'ERROR'),
                    ('message', 'MESSAGE')
                ], default='message', max_length=20, verbose_name='Type')),
                ('delivered', models.BooleanField(default=False, verbose_name='Delivered')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Key')),
                ('value', models.CharField(max_length=200, verbose_name='Value')),
                ('autoload', models.BooleanField(default=False, verbose_name='Autoload')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('github_url', models.CharField(max_length=100, verbose_name='Github URL')),
                ('facebook_url', models.CharField(max_length=100, verbose_name='Facebook URL')),
                ('twitter_url', models.CharField(max_length=100, verbose_name='Twitter URL')),
                ('access_token', models.CharField(max_length=200, verbose_name='Access token')),
                ('refresh_token', models.CharField(max_length=200, verbose_name='Refresh token')),
                ('access_token_updated_at', models.DateTimeField(null=True, verbose_name='Access token last update')),
                ('refresh_token_updated_at', models.DateTimeField(null=True, verbose_name='Refresh token last update')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Related user'
                )),
            ],
        ),
        migrations.CreateModel(
            name='Register_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=60, verbose_name='Email')),
                ('token', models.CharField(db_index=True, max_length=200, verbose_name='Token')),
                ('payload', models.CharField(max_length=200, verbose_name='Payload')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('expire_at', models.DateTimeField(verbose_name='Expire at')),
            ],
        ),
        migrations.CreateModel(
            name='Reset_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(db_index=True, max_length=60, verbose_name='Email')),
                ('token', models.CharField(db_index=True, max_length=200, verbose_name='Token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('expire_at', models.DateTimeField(verbose_name='Expire at')),
                ('messages_count', models.PositiveSmallIntegerField(verbose_name='Messages Count')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=60, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=60, verbose_name='Phone')),
                ('endpoint', models.CharField(max_length=200, verbose_name='Endpoint')),
                ('auth_token', models.CharField(max_length=200, verbose_name='Auth Token')),
                ('type', models.CharField(choices=[
                    ('email', 'EMAIL'),
                    ('phone', 'PHONE'),
                    ('endpoint', 'ENDPOINT')
                ], default='email', max_length=50, verbose_name='Type')),
                ('status', models.CharField(choices=[
                    ('pending', 'PENDING'),
                    ('verified', 'VERIFIED'),
                    ('unverified', 'UNVERIFIED')
                ], default='pending', max_length=50, verbose_name='Status')),
                ('external_id', models.CharField(max_length=200, verbose_name='External ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=200, verbose_name='UUID')),
                ('status', models.CharField(choices=[
                    ('pending', 'PENDING'),
                    ('failed', 'FAILED'),
                    ('passed', 'PASSED'),
                    ('error', 'ERROR')
                ], default='pending', max_length=20, verbose_name='Status')),
                ('executor', models.CharField(max_length=200, verbose_name='Executor')),
                ('parameters', models.TextField(verbose_name='Parameters')),
                ('result', models.TextField(verbose_name='Result')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Related user'
                )),
            ],
        ),
        migrations.CreateModel(
            name='User_Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=30, verbose_name='Meta key')),
                ('value', models.CharField(max_length=200, verbose_name='Meta value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Related User'
                )),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='task',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='app.Task',
                verbose_name='Related Task'
            ),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Related user'
            ),
        ),
        migrations.AddField(
            model_name='incident_update_notification',
            name='subscriber',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='app.Subscriber',
                verbose_name='Related Subscriber'
            ),
        ),
        migrations.AddField(
            model_name='component',
            name='group',
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='app.Component_Group',
                verbose_name='Related Component Group'
            ),
        ),
    ]
