def traducao(n):
    traducao1 = input()
    if n[::-1] == traducao1:
        print('Boa Deivis!')
    else:
        print('Poxa Deivis...')

traducao(input())