# Generated by Django 2.0.3 on 2018-04-02 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('area', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='buys',
            fields=[
                ('buy_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('invoice', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.branch')),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('phone_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('mob_no', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('mob_no', models.BigIntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.branch')),
            ],
        ),
        migrations.CreateModel(
            name='ins_company',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ins_policy',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('emi', models.IntegerField()),
                ('ins_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.ins_company')),
            ],
        ),
        migrations.CreateModel(
            name='manufacturer',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='model',
            fields=[
                ('model_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('release_date', models.DateField()),
                ('top_speed', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.branch')),
                ('mfg_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('reg_date', models.DateField()),
                ('reg_place', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sold',
            fields=[
                ('sale_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('sale_date', models.DateField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.branch')),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.model')),
            ],
        ),
        migrations.CreateModel(
            name='transportation',
            fields=[
                ('t_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('t_date', models.DateField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.branch')),
                ('mfg_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='registration',
            name='sale_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.sold'),
        ),
        migrations.AddField(
            model_name='ins_policy',
            name='sale_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.sold'),
        ),
        migrations.AddField(
            model_name='buys',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.customer'),
        ),
        migrations.AddField(
            model_name='buys',
            name='sale_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.sold'),
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdms.company'),
        ),
        migrations.AlterUniqueTogether(
            name='ins_policy',
            unique_together={('id', 'ins_company', 'sale_id')},
        ),
        migrations.AlterUniqueTogether(
            name='branch',
            unique_together={('area', 'phone_no')},
        ),
    ]
