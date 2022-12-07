from fastfood.models import *

client1 = Client(user=User.objects.create(email='nikname21@gmail.com', password='defender42'), name=' Азат Соколов', card_number='4147565798789009')
client1.save()

worker1 = Worker(user=User.objects.create(email='altywa1998@gmail.com', password='nono34'), name='Алтынай Алиева', position='Оператор кассы')
worker1.save()

shawarma = Food.objects.create(name='Shawarma', start_price=50)
burger = Food.objects.create(name='Burger', start_price=25)
cheese = Ingredient.objects.create(name='cheese', extra_price=10)
chicken = Ingredient.objects.create(name='chicken', extra_price=70)
meat = Ingredient.objects.create(name='meat', extra_price=80)
salad = Ingredient.objects.create(name='salad', extra_price=15)
fries = Ingredient.objects.create(name='fries', extra_price=15)

shawarma.booking.set([cheese, salad, fries], through_defaults={'client': client1, 'worker': worker1})
burger.booking.set([chicken, salad], through_defaults={'client': client1, 'worker': worker1})

shawarma.booking.all()
burger.booking.all()

res = (shawarma.start_price+cheese.extra_price+salad.extra_price+fries.extra_price)
res

res1 = (burger.start_price+salad.extra_price+chicken.extra_price)
res1

amount = (shawarma.start_price+burger.start_price+cheese.extra_price+salad.extra_price+fries.extra_price+chicken.extra_price+salad.extra_price)
amount









