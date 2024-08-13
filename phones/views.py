from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get("sort")
    phones_obj = Phone.objects.all()
    data_list = []
    for ph in phones_obj:
        phone = {
            'id': ph.id,
            'name': ph.name,
            'price': ph.price,
            'image': ph.image,
            'lte_exists': ph.lte_exists,
            'release_date': ph.release_date,
            'slug': ph.slug,
        }
        data_list.append(phone)
    if sort == 'name':
        sorted_list = []
        sorted_names = sorted([x["name"] for x in data_list])
        for name in sorted_names:
            for x in data_list:
                if name == x["name"]:
                    sorted_list.append(x)
    elif sort == 'min_price':
        sorted_list = []
        sorted_price = sorted([x["price"] for x in data_list])
        for price in sorted_price:
            for x in data_list:
                if price == x["price"]:
                    sorted_list.append(x)
    else:
        sorted_list = []
        sorted_price = sorted([x["price"] for x in data_list], reverse=True)
        for price in sorted_price:
            for x in data_list:
                if price == x["price"]:
                    sorted_list.append(x)
    context = {
        'phones': sorted_list
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    ph = Phone.objects.filter(slug=slug)[0]
    phone = {
        'id': ph.id,
        'name': ph.name,
        'price': ph.price,
        'image': ph.image,
        'lte_exists': ph.lte_exists,
        'release_date': ph.release_date,
        'slug': ph.slug,
    }
    context = {
        'phone': phone
    }
    return render(request, template, context)
