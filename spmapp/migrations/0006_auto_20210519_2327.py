# Generated by Django 3.2 on 2021-05-19 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spmapp', '0005_dataentry2addingassessmentdata_t_dataentry2addingnevalautiondata_t_dataentry2addingnewcourseinformat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='dataentry2AddingAssessmentdata_T',
        ),
        migrations.RemoveField(
            model_name='dataentry2addingnevalautiondata_t',
            name='section',
        ),
        migrations.RemoveField(
            model_name='dataentry2addingnevalautiondata_t',
            name='student',
        ),
        migrations.RemoveField(
            model_name='dataentry2addingnewcourseinformation_t',
            name='section',
        ),
        migrations.DeleteModel(
            name='dataentry2mappingPloToCo_T',
        ),
        migrations.DeleteModel(
            name='dataentry2AddingnEvalautionData_T',
        ),
        migrations.DeleteModel(
            name='dataentry2AddingnewCourseinformation_T',
        ),
    ]