print('\n\033[34m{:=^30}\033[m'.format('CONVERSOR DE METROS'))
M = float(input('Digite o valor em (Metros): '))
print('\033[32mQuilômetro: \033[m{}\n\033[32mHectômetro: \033[m{}\n\033[32m'
      'Decametro: \033[m{}\n\033[32mMetros: \033[m{}\n\033[32mDecimetro: \033[m{}\n\033[32m'
      'Centimetros: \033[m{}\n\033[32mMilimetros: \033[m{}'.format(M/1000, M/100, M/10, M, M*10, M*100, M*1000))
