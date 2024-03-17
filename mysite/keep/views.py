from django.shortcuts import render, redirect
from .models import Note
# Create your views here.

def mainpage(request):
    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            note = Note.objects.create(text=text)
            note.save()
        return redirect('mainpage')
    else:
        notes_list = Note.objects.order_by("last_modified")
        context = {
            "notes_list": notes_list,
        }
        return render(request, "keep/index.html", context)

def delete(request):
    if(request.method == "POST"):
        note_text = request.POST.get('del_text')
        mod_time = request.POST.get('del_time')
        note = Note.objects.get(text=note_text, last_modified=mod_time)
        if(note):
            note.delete()
        return redirect('mainpage')

def edit(request):
    if(request.method == "POST"):
        note_text = request.POST.get('edit_text')
        note_time= request.POST.get('edit_time')
        if(note_time):
            context = {
                "note_text": note_text
            }
            for i in Note.objects.all():
                print(i.last_modified)
            note = Note.objects.get(text=note_text, last_modified=note_time)
            note.delete()
            return render(request, "keep/edit.html", context)
        else:
            if note_text:
                note = Note.objects.create(text=note_text)
                note.save()
                return redirect('mainpage')
            return redirect('mainpage')