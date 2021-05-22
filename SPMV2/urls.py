"""SPMV2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from spmapp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.homeview, name='homepage'),
    path('admin/', admin.site.urls),
    path('login/', views.loginview, name='loginpage'),
    path('logout', views.logoutview, name='logoutpage'),


    path('cowise',views.cowiseplo,name='cowiseplo'),
    path('coursewise',views.coursewiseplo,name='coursewiseplo'),
    path('plotable',views.plotable,name='plotable'),

    path('dataentry',views.dataentry,name='dataentry'),


    #path('dataentry',views.dataentry,name='dataentry'),
    #path('dataentry2',views.dataentry2,name='dataentry2'),
    #path('dataentry2',views.plotoCoMapping,name='dataentry2'),
    #path('dataentry2',views.AssessmentDataEntry,name='dataentry2'),
    #path('dataentry2',views.EvaluationDataEntry,name='dataentry2'),


    ##path('courseverdict',views.courseverdict, name='courseverdict'),
    
    
    path('courseinfoentry',views.courseinfoentry,name='courseinfoentry'),
    path('plocomapping',views.plocomapping,name='plocomapping'),
    path('assessmentdataentry',views.assessmentdataentry,name='assessmentdataentry'),
    path('evaluationdataentry',views.evaluationdataentry,name='evaluationdataentry'),

    path('userprofile',views.userprofile, name='profile'),

    path('enrollment', views.enrollment, name='enrollment'),
    path('sgpa',views.semesterwisegpa, name='sgpa'),
    path('cgpa',views.coursewisegpa,name='cgpa'),
    path('igpa',views.instructorwisegpa, name='igpa'),
    path('lgpa', views.leaderwisegpa, name='lgpa'),
    path('cigpa',views.instructorwisegpaforcourse,name='cigpa'),

    path('stplo', views.studentplo, name='stplo'),
    path('pplo', views.programplo, name='pplo'),

    path('dplo', views.deptplo, name='dplo'),
    path('splo', views.schoolplo, name='splo'),

    path('stcomp',views.studentplocomp,name='stcomp'),
    path('ccomp', views.courseplocomp, name='ccomp'),
    path('pcomp', views.programplocomp, name='pcomp'),
    path('dcomp', views.deptplocomp, name='dcomp'),
    path('scomp',views.schoolplocomp, name='scomp'),



    path('creport', views.coursereport, name='creport'),
    path('preport', views.programreport, name='preport'),
    path('dreport', views.deptreport, name='dreport'),
    path('sreport', views.schoolreport, name='sreport'),

    path('pplostats',views.programwiseplostats,name='pplostats'),
    path('dplostats',views.deptwiseplostats,name='dplostats'),
    path('splostats',views.schoolwiseplostats,name='splostats'),

    path('studentplotable',views.studentplotable,name='studentplotable'),




]
