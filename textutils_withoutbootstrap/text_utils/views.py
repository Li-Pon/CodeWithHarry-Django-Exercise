from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'Li Pon', 'place': 'Mars'}
    return render(request,'index.html', params)


def analyze(request):
    text_area_text = request.GET.get('text', 'default')
    # ---
    punctuation_check = request.GET.get('punctuation', 'default')
    full_capital_check = request.GET.get('full_capital', 'default')
    new_line_remover_check = request.GET.get('new_line_remover', 'default')
    extra_space_check = request.GET.get('extraspace', 'default')
    charecter_counter_check = request.GET.get('char_counter', 'default')
    # ---
    if punctuation_check == 'on':
        punctuation_marks = '''.,?;!:'()[]"_-/@#$%^&*}{~'''
        analyzed = ""
        for char in text_area_text:
            if char not in punctuation_marks:
                analyzed += char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif full_capital_check == 'on':
        analyzed = ""
        for char in text_area_text:
            analyzed += char.upper()
        params = {'purpose': 'Full Capital', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif new_line_remover_check == 'on':
        analyzed = ""
        for char in text_area_text:
            if char != "\n":
                analyzed += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extra_space_check == 'on':
        analyzed = ""
        for char in text_area_text:
            if char != "  ":
                analyzed += char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charecter_counter_check == 'on':
        analyzed = 0
        for char in text_area_text:
            if char != " ":
                analyzed += 1
        params = {'purpose': 'Charecter Counter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Enter any box")
