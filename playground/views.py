from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Leitet zur Liste aller Bücher weiter
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
