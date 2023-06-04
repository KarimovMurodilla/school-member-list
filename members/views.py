from django.views.generic import ListView, DetailView

from .models import Teacher, Pupil, Lesson, Subject, ClassNumber


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
    template_name = 'members/teachers.html'


class PupilListView(ListView):
    model = Pupil
    template_name = 'members/pupils.html'


class ContactListView(ListView):
    template_name = 'members/contact.html'

    def get_queryset(self):
        return None


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


class LessonDetailView(DetailView):
    model = Subject
    template_name = 'members/lesson_detail.html'
