from django.shortcuts import render, redirect
from library.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.db.models import Q


# def clean(self):
#   start_date = self.cleaned_data['start_date']
#  end_date = self.cleaned_data['end_date']

# if end_date <= start_date:
#    raise forms.ValidationError("End date must be later than start date")
# return super(YourFormClass, self).clean()
def check(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        place = request.POST['place']
        time1 = request.POST['time1']
        time2 = request.POST['time2']
        day1 = request.POST['day1']
        # start = Table.objects.filter(Q(day=day1) & Q(place=place)).values('start')
        # end = Table.objects.filter(Q(day=day1) & Q(place=place)).values('end')

        schedules = Table.objects.filter(day=day1, place=place)
        # start = q1.filter(place=place).values('start')
        # q2 = Table.objects.filter(day=day1)
        # end = q2.filter(place=place).values('end')
        flag = 0
        x = ''
        time1 = datetime.strptime(time1, '%H:%M').time()
        time2 = datetime.strptime(time2, '%H:%M').time()
        for schedule in schedules:
            if time1 > time2:
                flag += 1
                x = ', because of you entered start bigger than end '
            elif time1 == schedule.start:
                flag += 1
            elif schedule.start < time1 < schedule.end:
                flag += 1
            elif time1 < schedule.start < time2:
                flag += 1
        if flag == 0:
            table1 = Table(name=name, day=day1, subject=subject, place=place, start=time1, end=time2)
            table1.save()
            messages.success(request, f"You managed to book {place} Prof {name}.")
        else:
            messages.success(request,
                             f"You can't book at this time Prof {name}{x}and you need to check the schedule out.")
        return render(request, 'schedule.html')
    else:
        return render(request, 'schedule.html')
        # start1 = datetime.strptime(time1, '%H:%M:%S').time()

        # if Table.objects.exclude(time1__gte=start,time1__lte=end):
        # if Table.objects.filter(time1__gte=start, time1__lte=end).exists():


# if Table.objects.filter(start1__range=(start[i], end[j])).exists():
#   messages.error(request, "You can't start on this time because it's reserved")
#  if Table.objects.filter(end1__range=(start[i], end[j])).exists():
#     messages.error(request, "You can't end on this time because it's reserved")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user1 = User(username=username, password=password, email=email)
        user1.save()
        return render(request, 'sign.html')
    return render(request, template_name='registration.html')


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user2 = authenticate(request, username=username, password=password)
        if user2 is not None:
            login(request, user2)
            return render(request, 'index.html')
    else:
        return render(request, 'sign.html')


def logout_request(request):
    logout(request)
    return redirect("/index/")


def sun(request):
    q1 = Table.objects.filter(day='Sunday')
    return render(request, 'table.html', {'table': q1})


def mon(request):
    q1 = Table.objects.filter(day='Monday')
    return render(request, 'table.html', {'table': q1})


def tue(request):
    q1 = Table.objects.filter(day='Tuesday')
    return render(request, 'table.html', {'table': q1})


def wed(request):
    q1 = Table.objects.filter(day='Wednesday')
    return render(request, 'table.html', {'table': q1})


def thu(request):
    q1 = Table.objects.filter(day='Thursday')
    return render(request, 'table.html', {'table': q1})


def index(request):
    return render(request, 'index.html')


def table(request):
    return render(request, 'table.html')


def days(request):
    return render(request, 'days.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name1']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print(name)
        table1 = Contact(name1=name, subject=subject, email=email, message=message)
        table1.save()
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def logout_request(request):
    logout(request)
    return redirect("/index/")


def prof(request):
    x = Table.objects.distinct()
    return render(request, 'prof.html', {'table': x})

