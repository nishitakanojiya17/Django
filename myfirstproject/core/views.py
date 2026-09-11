from django.shortcuts import render


def home(request):

    students = [
        'Aman',
        'Rahul',
        'Priya'
    ]

    return render(
        request,
        'home/index.html',
        {
            'students': students
        }
    )