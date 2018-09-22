#cat/dog age calculator

print ('1)cat or 2)dog')
select = input()
select = int(select)

if select== 1:
    print ('Cat age calculator\n')

    CatAge = int(input('what is you cats age in normal / human years\n'))

    RealCat = CatAge * 7
    RealCat =str(RealCat)
    print ('Your Cat is ' + RealCat + ' in Cat years\n')


if select==2:
    print ('dog age calculator\n')

    CatAge = int(input('what is you dogs age in normal / human years\n'))

    RealCat = CatAge * 7
    RealCat =str(RealCat)
    print ('Your dog is ' + RealCat + ' in dog years\n')


a=input('press RETURN to close')
