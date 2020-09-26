p_money = int(input("Введите сумму выручки -> "))
m_money = int(input("Введиде сумму издержек -> "))
v_money = int(p_money - m_money)
if p_money > m_money:
    print(f"Вы получили {v_money} прибыли")
    workers = int(input("Введите кол-во ваших сотрудников ->"))
    raschet = int(v_money // workers)
    print(f"Сумма прибыли на 1 сотрудника составляет {raschet}")
else:
    print("Вы работаете в убыток, нам вас жаль Т_Т")
