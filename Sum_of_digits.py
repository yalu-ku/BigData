# 자리수의 합을 계산하는 프로그램
# 연산자 //를 사용
print("="*9)
num = int(input('네자리 이하로 정수를 입력하시오.'))
# sum = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])
n_1 = num // 1000
n_10 = str(num // 100)
n_100 = str(num // 10)
n_1000 = str(num // 1)
sum = n_1 + int(n_10[1]) + int(n_100[2]) + int(n_1000[3])
print('자리수의 합=', sum)

