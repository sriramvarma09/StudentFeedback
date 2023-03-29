from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('cse-1year', views.cse_1),
    path('cse-2year', views.cse_2),
    path('cse-3year', views.cse_3),
    path('cse-4year', views.cse_4),

    path('csit-1year', views.csit_1),
    path('csit-2year', views.csit_2),
    path('csit-3year', views.csit_3),
    path('csit-4year', views.csit_4),

    path('csse-1year', views.csse_1),
    path('csse-2year', views.csse_2),
    path('csse-3year', views.csse_3),
    path('csse-4year', views.csse_4),


    path('ece-1year', views.ece_1),
    path('ece-2year', views.ece_2),
    path('ece-3year', views.ece_3),
    path('ece-4year', views.ece_4),

    path('eee-1year', views.eee_1),
    path('eee-2year', views.eee_2),
    path('eee-3year', views.eee_3),
    path('eee-4year', views.eee_4),

    path('mech-1year', views.mech_1),
    path('mech-2year', views.mech_2),
    path('mech-3year', views.mech_3),
    path('mech-4year', views.mech_4),



    path('cse-a:feedback', views.subject_1, name="subject_1"),
    path('cse-b:feedback', views.subject_1, name="subject_1"),
    path('cse-c:feedback', views.subject_1, name="subject_1"),



    path('csit:feedback', views.subject_1, name="subject_1"),
    # path('csit-b:feedback',views.subject_1,name="subject_1"),
    # path('csit-c:feedback',views.subject_1,name="subject_1"),


    path('csse:feedback', views.subject_1, name="subject_1"),
    # path('cse-b:feedback',views.subject_1,name="subject_1"),
    # path('cse-c:feedback',views.subject_1,name="subject_1"),

    path('ece-a:feedback', views.subject_1, name="subject_1"),
    path('ece-b:feedback', views.subject_1, name="subject_1"),
    path('ece-c:feedback', views.subject_1, name="subject_1"),


    path('eee-a:feedback', views.subject_1, name="subject_1"),
    path('eee-b:feedback', views.subject_1, name="subject_1"),
    # path('eee-c:feedback',views.subject_1,name="subject_1"),

    path('mech-a:feedback', views.subject_1, name="subject_1"),
    path('mech-b:feedback', views.subject_1, name="subject_1"),
    # path('mech-c:feedback',views.subject_1,name="subject_1"),






    path('subject_2', views.subject_2, name="subject_2"),
    path('subject_3', views.subject_3, name="subject_3"),
    path('subject_4', views.subject_4, name="subject_4"),
    path('subject_5', views.subject_5, name="subject_5"),
    #path('thanku', views.thanku, name="thanku")

    path('details', views.details, name="details")






]
