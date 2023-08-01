with open("Names.txt",'r') as ppl:
    names = ppl.read().split('\n')
    for i in names:
        with open("mail.txt", 'r') as bdi:
            inv = bdi.read().replace('[name]', i)
            with open(f'Ready_To_Send/Birtjday_Invitation_{i}.txt', 'w') as tst1:
                tst1.write(inv)


