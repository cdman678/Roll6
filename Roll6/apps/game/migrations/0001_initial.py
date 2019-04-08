# Generated by Django 2.2 on 2019-04-08 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('resource', models.BooleanField()),
                ('red_tape', models.BooleanField()),
                ('option', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_class', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DarkSide',
            fields=[
                ('tag_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fate',
            fields=[
                ('fate_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('heroic', models.BooleanField()),
                ('doom', models.BooleanField()),
                ('fate_tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('game_ID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=30)),
                ('user_ID', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('last_run_date', models.DateTimeField(verbose_name='date last run')),
            ],
        ),
        migrations.CreateModel(
            name='Haven',
            fields=[
                ('haven_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Heat',
            fields=[
                ('heat_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('heat_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('who', models.BooleanField()),
                ('what', models.BooleanField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Sect',
            fields=[
                ('sect_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('good', models.BooleanField()),
                ('bad', models.BooleanField()),
                ('sect_tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Spells',
            fields=[
                ('spell_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('base', models.BooleanField()),
                ('effect', models.BooleanField()),
                ('spell_name', models.CharField(max_length=20)),
                ('spell_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Underworld',
            fields=[
                ('underworld_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('underworld_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('gear_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('weapon_name', models.CharField(max_length=20)),
                ('damage', models.IntegerField()),
                ('mechanic', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('gear_ID', 'weapon_name')},
            },
        ),
        migrations.CreateModel(
            name='AssignedGear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear_ID', models.IntegerField()),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CharacterClasses')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('rating_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('charm_modifier', models.IntegerField()),
                ('cool_modifier', models.IntegerField()),
                ('sharp_modifier', models.IntegerField()),
                ('tough_modifier', models.IntegerField()),
                ('weird_modifier', models.IntegerField()),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CharacterClasses')),
            ],
            options={
                'unique_together': {('rating_ID', 'char_class')},
            },
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('move_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('move_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('default', models.BooleanField()),
                ('mechanics', models.CharField(max_length=100)),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CharacterClasses')),
            ],
            options={
                'unique_together': {('move_ID', 'char_class')},
            },
        ),
        migrations.CreateModel(
            name='Improvements',
            fields=[
                ('improvement_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('text_improvement', models.CharField(max_length=20)),
                ('charm_modifier', models.IntegerField()),
                ('cool_modifier', models.IntegerField()),
                ('sharp_modifier', models.IntegerField()),
                ('tough_modifier', models.IntegerField()),
                ('weird_modifier', models.IntegerField()),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CharacterClasses')),
            ],
            options={
                'unique_together': {('improvement_ID', 'char_class')},
            },
        ),
        migrations.CreateModel(
            name='AdvImprovements',
            fields=[
                ('improvement_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('improvement', models.CharField(max_length=100)),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CharacterClasses')),
            ],
            options={
                'unique_together': {('improvement_ID', 'char_class')},
            },
        ),
        migrations.CreateModel(
            name='ActiveGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=99999)),
                ('charm', models.IntegerField()),
                ('cool', models.IntegerField()),
                ('sharp', models.IntegerField()),
                ('tough', models.IntegerField()),
                ('weird', models.IntegerField()),
                ('luck', models.IntegerField()),
                ('harm', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('move_list', models.CharField(max_length=100)),
                ('weapon_list', models.CharField(max_length=100)),
                ('history_list', models.CharField(max_length=100)),
                ('improvements_list', models.CharField(max_length=100)),
                ('advImprovements_list', models.CharField(max_length=100)),
                ('char_specific', models.CharField(max_length=100)),
                ('char_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.CharacterClasses')),
                ('game_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
            ],
            options={
                'unique_together': {('game_ID', 'char_class')},
            },
        ),
    ]
