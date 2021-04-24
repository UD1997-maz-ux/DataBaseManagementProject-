# Generated by Django 3.2 on 2021-04-24 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment_T',
            fields=[
                ('AssessmentID', models.AutoField(primary_key=True, serialize=False)),
                ('AssessmentName', models.CharField(max_length=30)),
                ('QuestionNum', models.IntegerField()),
                ('TotalMarks', models.FloatField()),
                ('Weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_T',
            fields=[
                ('CourseID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('CourseName', models.CharField(max_length=50, null=True)),
                ('NumOfCredits', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Department_T',
            fields=[
                ('DepartmentID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_T',
            fields=[
                ('FirstName', models.CharField(max_length=30, null=True)),
                ('LastName', models.CharField(max_length=30, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('Gender', models.CharField(max_length=6, null=True)),
                ('Email', models.CharField(max_length=30, null=True)),
                ('Phone', models.CharField(max_length=15, null=True)),
                ('Address', models.CharField(max_length=30, null=True)),
                ('EmployeeType', models.CharField(max_length=1, null=True)),
                ('FacultyID', models.IntegerField(primary_key=True, serialize=False)),
                ('StartDate', models.DateField(null=True)),
                ('Rank', models.CharField(max_length=50, null=True)),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program_T',
            fields=[
                ('ProgramID', models.AutoField(primary_key=True, serialize=False)),
                ('ProgramName', models.CharField(max_length=70)),
                ('DepartmentID', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
            ],
        ),
        migrations.CreateModel(
            name='School_T',
            fields=[
                ('SchoolID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('SchoolName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VC_T',
            fields=[
                ('FirstName', models.CharField(max_length=30, null=True)),
                ('LastName', models.CharField(max_length=30, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('Gender', models.CharField(max_length=6, null=True)),
                ('Email', models.CharField(max_length=30, null=True)),
                ('Phone', models.CharField(max_length=15, null=True)),
                ('Address', models.CharField(max_length=30, null=True)),
                ('EmployeeType', models.CharField(max_length=1, null=True)),
                ('VCID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student_T',
            fields=[
                ('StudentID', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50, null=True)),
                ('LastName', models.CharField(max_length=50, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('Gender', models.CharField(max_length=6, null=True)),
                ('Email', models.CharField(max_length=50, null=True)),
                ('Phone', models.CharField(max_length=15, null=True)),
                ('Address', models.CharField(max_length=50, null=True)),
                ('EnrollmentDate', models.DateField(null=True)),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
                ('ProgramID', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.program_t')),
            ],
        ),
        migrations.CreateModel(
            name='Section_T',
            fields=[
                ('ScetionID', models.AutoField(primary_key=True, serialize=False)),
                ('SectionNum', models.IntegerField()),
                ('Semester', models.CharField(max_length=6)),
                ('Year', models.IntegerField()),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.course_t')),
                ('FacultyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.faculty_t')),
            ],
        ),
        migrations.CreateModel(
            name='Registration_T',
            fields=[
                ('RegistrationID', models.AutoField(primary_key=True, serialize=False)),
                ('Semester', models.CharField(max_length=6)),
                ('Year', models.IntegerField()),
                ('SectionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.section_t')),
                ('StudentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.student_t')),
            ],
        ),
        migrations.CreateModel(
            name='PrereqCourse_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Course', to='spmapp.course_t')),
                ('PreReqCourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PreRequisite', to='spmapp.course_t')),
            ],
        ),
        migrations.CreateModel(
            name='PLO_T',
            fields=[
                ('PLOID', models.AutoField(primary_key=True, serialize=False)),
                ('PLONum', models.CharField(max_length=5)),
                ('Details', models.CharField(max_length=50)),
                ('ProgramID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.program_t')),
            ],
        ),
        migrations.CreateModel(
            name='Head_T',
            fields=[
                ('FirstName', models.CharField(max_length=30, null=True)),
                ('LastName', models.CharField(max_length=30, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('Gender', models.CharField(max_length=6, null=True)),
                ('Email', models.CharField(max_length=30, null=True)),
                ('Phone', models.CharField(max_length=15, null=True)),
                ('Address', models.CharField(max_length=30, null=True)),
                ('EmployeeType', models.CharField(max_length=1, null=True)),
                ('HeadID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField(null=True)),
                ('DepartmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.department_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluation_T',
            fields=[
                ('EvaluationID', models.AutoField(primary_key=True, serialize=False)),
                ('ObtainedMarks', models.FloatField()),
                ('AssessmentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.assessment_t')),
                ('RegistrationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.registration_t')),
            ],
        ),
        migrations.AddField(
            model_name='department_t',
            name='SchoolID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.school_t'),
        ),
        migrations.CreateModel(
            name='Dean_T',
            fields=[
                ('FirstName', models.CharField(max_length=30, null=True)),
                ('LastName', models.CharField(max_length=30, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('Gender', models.CharField(max_length=6, null=True)),
                ('Email', models.CharField(max_length=30, null=True)),
                ('Phone', models.CharField(max_length=15, null=True)),
                ('Address', models.CharField(max_length=30, null=True)),
                ('EmployeeType', models.CharField(max_length=1, null=True)),
                ('DeanID', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField(null=True)),
                ('SchoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.school_t')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course_t',
            name='ProgramID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.program_t'),
        ),
        migrations.CreateModel(
            name='CO_T',
            fields=[
                ('COID', models.AutoField(primary_key=True, serialize=False)),
                ('CONum', models.CharField(max_length=4)),
                ('Thresold', models.FloatField(default=40)),
                ('CourseID', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.course_t')),
                ('PLOID', models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='spmapp.plo_t')),
            ],
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='COID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.co_t'),
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='SectionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spmapp.section_t'),
        ),
    ]