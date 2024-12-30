from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

def home(request):
    trans = translate(language='fr')
    return render(request, 'home.html', {'trans': trans})

def item(request):
    trans = _('hello')
    return render(request, 'item.html', {'trans': trans})

def translate(language):
    cur_language = get_language()
    try:
        # Activate the new language
        activate(language)
        
        # Get translations for both 'hello' and 'good'
        hello_trans = gettext('hello')
        good_trans = gettext('Good')
        
    finally:
        # Reset to the original language
        activate(cur_language)
    
    # Return both translations as a dictionary
    return {'hello': hello_trans, 'Good': good_trans}
