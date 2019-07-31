from django.shortcuts import render
from .models import StudentFeedback
from .forms import FeedbackForm, ModelFormCreation
import random
import os
# Create your views here.
ID_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'my_data.txt')
def id_generator():
	with open(ID_FILE_PATH, 'a+') as my_file:
		my_file.seek(0)		
		l = my_file.readline().strip()
		if(not l):
			id = my_file.write('1')
			return 1	
		else:
			# print(l)
			val = int(l, 10) + 1
			my_file.seek(0)
			print('after seek')
			my_file.truncate()
			print('file truncate')
			my_file.write(str(val))
			print('updated')
			return val    

def model_form_creation(request):
	form = ModelFormCreation()
	if request.method == 'POST':
		form = ModelFormCreation(request.POST)
		if form.is_valid():
			form.save()
	
	return render(request, 'eighth_app/model_form_creation.html', {'model_form': form.as_p})

def index(request):
    feedbacks = StudentFeedback.objects.all()
    form = FeedbackForm()

    if request.method == 'POST':
    	form = FeedbackForm(request.POST)
    	if form.is_valid():
		    # student_id = random.randint(1, 100000)
		    student_id = id_generator()
		    name = form.cleaned_data['name']
		    course = form.cleaned_data['course']
		    email = form.cleaned_data['email']
		    feedback = form.cleaned_data['feedback']	    
		    s = StudentFeedback(student_id, name, course, email, feedback)
		    s.save()	    
	     	    

    my_dict = {'greetings': 'Hi Abhishek', 'students_feedback': feedbacks, 'feedback_form': form.as_p}
    
    return render(request, 'eighth_app/index.html', context = my_dict)