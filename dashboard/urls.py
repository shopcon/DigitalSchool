from django.conf.urls import patterns, include, url


urlpatterns=[
    url(r'login/$', 'dashboard.views.login_view', name='Login View'),
    url(r'logout/$', 'dashboard.views.logout_view', name='Logout View'),

    url(r'^$', 'dashboard.views.dashboard_view', name='Dashboard View'),
    url(r'counselling/$', 'dashboard.views.counselling_view', name='Our Counselling View'),

    url(r'ourgallery/$', 'dashboard.views.ourgallery_view', name='Our Gallery View'),
    url(r'testimonial/$','dashboard.views.testimonial_view',name='Testimonial View'),
    url(r'blog/$','dashboard.views.blog_view',name='Blog View'),
    url(r'photogallery/$', 'dashboard.views.addphoto_view', name='Add Photo View'),
    url(r'mediagallery/$', 'dashboard.views.media_view', name='Add Media View'),
    url(r'ourgallery/delete/(?P<string1>\d+)/$', 'dashboard.views.delete_ourgallery_view', name='Delete Our Gallery View'),
    url(r'photogallery/delete/(?P<string1>\d+)/$', 'dashboard.views.delete_photogallery_view',
        name='Delete Photo Gallery View'),
    url(r'mediagallery/delete/(?P<string1>\d+)/$', 'dashboard.views.delete_mediagallery_view',
        name='Delete Media Gallery View'),
    url(r'blog/delete/(?P<string1>\d+)/$', 'dashboard.views.delete_blog_view',
        name='Delete Blog View'),
]