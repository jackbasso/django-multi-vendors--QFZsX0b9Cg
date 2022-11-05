# Making Cart available globally to show quantity next to Cart button in menu; add to SETTINGS too
from .cart import Cart

def cart(request):
  return {'cart': Cart(request)}