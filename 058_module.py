# import theater_module
# theater_module.price(3) #3명이서 영화보러 갔을때
# theater_module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을때
# theater_module.price_soldier(5) #5명의 군인이 영화보러 갔을때

# import theater_module as mv 
# # import module as modulename은 module을 modulename으로 호출할수 있게 해준다
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # from random import * 은 random모듈없이  *을 바로 사용할수있게해준다
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)

# from theater_module import price_soldier as price
# #price_soldier를 price로 사용할수있다
# price(4)
# price_morning(4)
# price_soldier(4)