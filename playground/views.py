from django.shortcuts import render, redirect
from .forms import BuchForm

def add_book(request):
    if request.method == 'POST':
        form = BuchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Leitet zur Liste aller Bücher weiter
    else:
        form = BuchForm()
    return render(request, 'add_book.html', {'form': form})
