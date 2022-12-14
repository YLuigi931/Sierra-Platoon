from .models import Product 

class ProductCrud:
    
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()
    
    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)

    @classmethod
    def last_record(cls):
        return Product.objects.last()
    
    @classmethod
    def by_rating(cls, by_rating):
        return Product.objects.filter(rating = by_rating)
    
    @classmethod
    def by_rating_range(cls, min, max):
        return Product.objects.filter(rating__range = (min,max))
    
    @classmethod
    def by_rating_and_color(cls, desired_rating, desired_color):
        return Product.objects.filter(rating = desired_rating, color = desired_color)
    
    @classmethod
    def by_rating_or_color(cls, desired_rating, desired_color ):
        return Product.objects.filter(rating = desired_rating, color = desired_color)| Product.objects.filter(rating = desired_rating, color = desired_color)
    
    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()
    
    @classmethod
    def below_price_or_above_rating(cls, below_rate, above_rate):
        return Product.objects.filter(rating__lt = below_rate)| Product.objects.filter(rating__gt = above_rate)
    
    
    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        return Product.objects.order_by('category', '-price_cents')
    