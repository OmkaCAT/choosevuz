from django.shortcuts import render, get_object_or_404, HttpResponse
from itertools import combinations, chain
from .models import University, Specialty, SpecialtyScoreForUniversity, Subject


# Create your views here.

def index(request):
    pages = 'index'
    return render(request, 'index.html', {'pages': pages})

def university_and_specialty_lists(request):
    specialties = Specialty.objects.all()
    universities = University.objects.all()
    return render(request, 'universities/base.html', {'specialties': specialties, 'universities': universities})


def specialty_list(request):
    pages = 'specialty'
    specialties = Specialty.objects.all()
    return render(request, 'universities/specialty_list.html', {'specialties': specialties, 'pages': pages})


def specialty_detail(request, pk):
    pages = 'specialty'
    specialty = get_object_or_404(Specialty, pk=pk)
    universities = SpecialtyScoreForUniversity.objects.filter(specialty=specialty)
    return render(request, 'universities/specialty_detail.html', {'specialty': specialty, 'universities': universities, 'pages': pages})


def university_list(request):
    pages = 'university'
    universities = University.objects.all()
    return render(request, 'universities/university_list.html', {'universities': universities, 'pages': pages})


def university_detail(request, pk):
    pages = 'university'
    university = get_object_or_404(University, pk=pk)
    specialties = SpecialtyScoreForUniversity.objects.filter(university=university)
    return render(request, 'universities/university_detail.html',
                  {'university': university, 'specialties': specialties, 'pages': pages})


def subjects_and_scores_search_form(request):
    pages = 'search_form'
    subjects = Subject.objects.all()
    return render(request, 'universities/search_form.html', {'subjects': subjects, 'pages': pages})


def subjects_and_scores_search(request):
    pages = 'search_form'
    subjects = request.GET.dict()
    subject_parsed = {}
    for subject_key in subjects:
        key = subject_key.split('_')
        if (subjects.get(subject_key) != ''):
            subject_parsed[key[1]] = subjects.get(subject_key)

    queries = combinations(subject_parsed.keys(), 3)

    final_list = {}
    for query in queries:
        specialties = SpecialtyScoreForUniversity.objects.all()
        score_sum = 0
        for subject in query:
            specialties = specialties.filter(subjects=subject)
            score_sum = score_sum + int(subject_parsed[subject])
        specialties = specialties.filter(score__lte=score_sum)
        final_list = chain(final_list, specialties)

    return render(request, 'universities/search.html', {'specialties': final_list, 'pages': pages})