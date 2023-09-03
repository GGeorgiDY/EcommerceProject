# тази функция изисква само owner-a да може да достъпва определени неща. Сиреч през инкогнито няма да мога да вляза и да променя дадени неща
# използва се за function based views
def is_owner(request, obj):
    return request.user == obj.user


# ако имахме вместо function based view, class based view, горната функция можеше да я направим като следния миксин:
# този миксин изисква само owner-a да може да достъпва определени неща. Сиреч през инкогнито няма да мога да вляза и да променя дадени неща
# използва се за class based views
class OwnerRequired:
    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)

        if request.user == self.object.user:
            return result
        else:
            return '...'