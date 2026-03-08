from .models import Category
from assignments.models import SocialLinks

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)
    
def get_social_links(request):
    socialLinks = SocialLinks.objects.all()
    return dict(socialLinks = socialLinks)