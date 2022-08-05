from django.shortcuts import render
from .thread import CreateStudentThread

# Create your views here.


# Threading
def create_student(request):
	count = 100
	# CreateStudentThread(count).start()
	return render(request, 'thread/createstu.html', {'count' : count})

