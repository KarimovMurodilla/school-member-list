from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Teacher, Pupil, Feedback, Subject, ClassNumber, Post

from .forms import FeedbackForm

class HomeListView(ListView):
    model = Teacher
    template_name = 'members/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pupil'] = Pupil.objects.all()
        return context


class AboutListView(ListView):
    template_name = 'members/about.html'

    def get_queryset(self):
        return None


class TeacherListView(ListView):
    model = Teacher
    ordering = ['id']
    template_name = 'members/teachers.html'


class PupilListView(ListView):
    model = Pupil
    ordering = ['id']
    template_name = 'members/pupils.html'


class ContactListView(ListView):
    template_name = 'members/contact.html'

    def get_queryset(self):
        return None


class EtiquetteListView(ListView):
    template_name = 'members/etiquette.html'

    def get_queryset(self):
        return None


class ClassNumberListView(ListView):
    model = ClassNumber
    template_name = 'members/lesson.html'


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'members/subject_detail.html'
    pk_url_kwarg = "classes__class_number"
    slug_field = "title"


# ---Posts---
class PostListView(ListView):
    model = Post
    template_name = "members/post.html"


# ---Feedback---
class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'members/contact.html'
    success_url = '/thank-you/'