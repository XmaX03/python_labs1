#Лабораторные работы

#Лабораторная работа №1
## Задание 1

```python
a = (input('Имя:'))
b = int(input('Возраст:'))
print('Привет,'+ str(a) + '! Через год тебе будет'+ str(b+1)+'.')
```
![Code](./images/lab01/01_greeting.png)

## Задание 2

```python
a = float(input("a: ").replace(',', '.'))
b = float(input("b: ").replace(',', '.'))
print(f"sum={a+b:.2f}; avg={(a+b)/2:.2f}")
```
![Code](./images/lab01/02_sum_avg.png)

## Задание 3

```python
price = int(input('Стоимость $:'))
discount = int(input('Скидка, %:'))
vat = int(input('НДС:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки:', base)
print('НДС:',vat_amount)
print('Итого к оплате:',total)
```
![Code](./images/lab01/03_discount_vat.png)

## Задание 4

```python
minutes_input = int(input('Минуты:'))
hour = 60
hours = minutes_input//hour
minutes = minutes_input-(hours*hour)
print(str(hours) + ':' + str(minutes))
```
![Code](./images/lab01/04_minutes_to_hhmm.png)

## Задание 5

```python
fio_input = input("ФИО: ")
fio_clean = ' '.join(fio_input.split())
words = fio_clean.split()
initials = ''.join([word[0].upper() for word in words])
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(fio_clean)}")
```
![Code](./images/lab01/05_initials_and_len.png)