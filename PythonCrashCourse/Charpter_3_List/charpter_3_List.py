__author__ = 'zhangedison'


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#访问列表元素
print(bicycles[0])

print(bicycles[0].title())

print(bicycles[1])

print(bicycles[3])

print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorycles_new = []
print(motorycles_new)
motorycles_new.append('honda_new')
motorycles_new.append('yamaha_new')
motorycles_new.append('suzuki_new')
print(motorycles_new)

motorycles_insert = ['honda_1', 'yamaha_2', 'suzuki_3']
motorycles_insert.insert(0, 'ducati_1')
print(motorycles_insert)

del motorycles_insert[0]
print(motorycles_insert)


motorycles_pop = ['honda_pop', 'yamaha_pop', 'suzuki_pop']
print(motorycles_pop)

popped_motorycles = motorycles_pop.pop()
print(motorycles_pop)
print(popped_motorycles)

motorycles_pop = ['honda_pop', 'yamaha_pop', 'suzuki_pop']
last_owned = motorycles_pop.pop()
print("The last motorycle I owned was a " + last_owned.title() + ".")


motorycles_pop = ['honda_pop', 'yamaha_pop', 'suzuki_pop']
first_owned = motorycles_pop.pop(0)
print("The first motorycle I owned was a " + first_owned.title() + ".")


motorycles_remove = ['honda_remove', 'yamaha_remove', 'suzuki_remove', 'ducati_remove']
print(motorycles_remove)
motorycles_remove.remove('ducati_remove')
print(motorycles_remove)

motorycles_remove = ['honda_remove', 'yamaha_remove', 'suzuki_remove', 'ducati_remove']
print(motorycles_remove)

too_expensive = 'ducati_remove'
motorycles_remove.remove(too_expensive)
print(motorycles_remove)
print("\nA " + too_expensive.title() + " is too expensive for me.")

################################################################
### 3.3.1

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

###########################
### 3.3.3
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

### 3.3.4
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
