from django.shortcuts import redirect
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.models.customer import Customer

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))
        print(address,phone,city,state,zip_code,phone,customer,cart,products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

