from django.urls import path
from ticketSales import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('concert/list', views.concertlistView),
    path('location/list', views.locationlistView),
    path('concert/<int:concert_id>', views.concertdetailsView),
    path('time/list', views.timeView),
    path('concertEdit/<int:concert_id>', views.concertEditView)

]