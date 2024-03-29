#n,m = map(int,input().split())
n = int(input("물건 가격 :"))
m = int(input("지불 가격 :"))
k = (m-n)//1000
a = (m-n)%1000//500
b = (m-n)%500//100
c = (m-n)%100//50

print("1000 :",k,", 500 :",a,", 100 :",b,", 50 :",c,", 총 개수 :",k+a+b+c)
