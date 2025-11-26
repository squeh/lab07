menu = int(input("""
Выберите напиток из меню (1-5) :
╔═══╦═══════════╦═════════════
  1 ║ Кофе      ║ 120 Рублей
╠═══╬═══════════╬════════════╣
  2 ║ Чай       ║ 80 Рублей
╠═══╬═══════════╬════════════╣
  3 ║ Сок       ║ 100 Рублей
╠═══╬═══════════╬════════════╣
  4 ║ Вода      ║ 50 Рублей
╠═══╬═══════════╬════════════╣
  5 ║Лимонад    ║ 120 Рублей
╚═══╩═══════════╩════════════
"""))
amount = int(input("Сколько порций вы будете? (напишите цифру) "))
discount = input("Введите промокод, если у вас он есть: ")

match menu:
    case 1:
        drink = "Кофе"
        emoji = "☕"
        cost_one = 120
        amount = amount
        if discount == "STUDENT":
            cost = int(amount * cost_one) * 0.8
            percent = "20%"
            costt = amount * cost_one
            cost_dis = amount - cost
        else:
            cost = amount * cost_one
            percent = "0%"
            cost_dis = "0"
            discount = "-"

    case 2:
        drink = "Чай"
        emoji = "🍵"
        cost_one = 80
        amount = amount
        if discount == "STUDENT":
            cost = int(amount * cost_one) * 0.8
            percent = "20%"
            costt = amount * cost_one
            cost_dis = amount - cost
        else:
            cost = amount * cost_one
            percent = "0%"
            cost_dis = "0"
            discount = "-"

    case 3:
        drink = "Сок"
        emoji = "🧃"
        cost_one = 100
        amount = amount
        if discount == "STUDENT":
            cost = int(amount * cost_one) * 0.8
            percent = "20%"
            cost = amount * cost_one
            cost_dis = amount - cost
        else:
            cost = amount * cost_one
            percent = "0%"
            cost_dis = "0"
            discount = "-"

    case 4:
        drink = "Вода"
        emoji = "🫗"
        cost_one = 50
        amount = amount
        if discount == "STUDENT":
            cost = int(amount * cost_one) * 0.8
            percent = "20%"
            costt = amount * cost_one
            cost_dis = amount - cost
        else:
            cost = amount * cost_one
            percent = "0%"
            cost_dis = "0"
            discount = "-"

    case 5:
        drink = "Лимонад"
        emoji = "🥤"
        cost_one = 90
        amount = amount
        if discount == "STUDENT":
            cost = int(amount * cost_one) * 0.8
            percent = "20%"
            costt = amount * cost_one
            cost_dis = amount - cost
        else:
            cost = amount * cost_one
            percent = "0%"
            cost_dis = "0"
            discount = "-"

    case _:
        drink = "ОШИБКА"
        emoji = "❌"
        cost_one = 1
        amount = amount
        costt = amount * cost_one
        percent = "0%"
        cost = ""


print(f"""
        ╔═══════════════════════════════════╗
                {emoji} КВИТАНЦИЯ КАФЕ {emoji}    ⠀      
        ╚═══════════════════════════════════╝

╔═══════╦════════════════════════════
  Товар ║ {drink} {emoji}
╠═══════╩════════╦═══════════════════
  Цена за порцию ║ {cost_one} руб.
╠════════╦═══════╩═══════════════════
  Кол-во ║ {amount} порции.
╠═══════╦╩═══════════════════════════
  Сумма ║ {cost} руб.
╠═══════╩╦═══════════════════════════
  СКИДКА ║ "{discount}" {percent} : {cost_dis} руб.
╠════════╩════╦══════════════════════
  💰 К ОПЛАТЕ ║ {cost} руб.
╚═════════════╩══════════════════════
 
""")
