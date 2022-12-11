from django.shortcuts import render, redirect

from .models import Notification


def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)
    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()
        return redirect('view_application', application_id=notification.extra_id)
    data = Notification.objects.all()
    stu = {
        "notification": data
    }
    return render(request, "notification/notifications.html", stu)