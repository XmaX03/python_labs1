price = int(input('Стоимость $:'))
discount = int(input('Скидка, %:'))
vat = int(input('НДС:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки:', base)
print('НДС:',vat_amount)
print('Итого к оплате:',total)