from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        try:
            tag = request.POST.get('tag')
            if tag != "":
                tag =tag
            note = Note(content=content,title=title,tag=tag)
        except:
            note = Note(content=content,title=title)
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def edit(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        try:
            tag = request.POST.get('tag')
        except:
            tag = ""
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        note = Note(content=content,title=title,tag=tag)
        note.save()
        return redirect('index')

    else:
         all_notes = Note.objects.all()
         return render(request, 'notes/edit.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id_delete')
        note = Note.objects.get(id=id)
        note.delete()
        return redirect("index")

def update(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        try:
            tag = request.POST.get('tag')
        except:
            tag = ""
        id = request.POST.get('id_update')
        note = Note.objects.filter(id=id)
        note.update(content=content,title=title,tag=tag)
        return redirect('index')

def tag_1(request):
    tags=Note.objects.all()
    tags = tags.values("tag")
    tags = list(dict.fromkeys([tag['tag'] for tag in tags if tag['tag']!=""]))
    return render(request,'notes/tag.html',{"tags":tags} )

def tag_2(request,tag):
    tags=Note.objects.all()
    tags = tags.filter(tag=tag)
    
    return render(request,'notes/tag-filter.html',{"notes":tags})
