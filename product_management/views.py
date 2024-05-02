from django.shortcuts import render
from .models import Product

def home_view(request):
    return render(request, 'home.html')


def add_product_view(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        # Veritabanına ürünü kaydet
        product = Product.objects.create(name=name, price=price, description=description)

        # Kayıt işlemi başarılı olduysa
        if product:
            submission_status = "Product successfully added to the database."
        else:
            submission_status = "Failed to add product to the database."
    else:
        submission_status = None
    
    return render(request, 'product_management_panel.html', {'submission_status': submission_status})


# Ürünleri listeleyen view fonksiyonu
def product_list_view(request):
    # Tüm ürünleri veritabanından al
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
