#줄바꿈 없는 출력
print('안녕', end="")
print('하세요')
#줄바꿈(\n은 기본값으로 생략되어 있음)
print('안녕\n하세요')

#int, float, str, bool
print(type(0))
print(type(1.1))
print(type('1'+'1'))
print(type(2>5))

#변수(값이 변할 수 있음)
My_name = '인수'
print(My_name) #인수

My_name = '10'
print(My_name) #10

#가격이 val인 물건을 살때 필요한 지폐, 동전의 수(10000원, 1000원, 100원 ,10원)
class auto_cal:
    def __init__(self, val, paper_1, paper_2, coin_1, coin_2):
        self.val = val
        self.paper_1 = paper_1
        self.paper_2 = paper_2
        self.coin_1 = coin_1
        self.coin_2 = coin_2

    def Calculation(self):
        count_paper_1 = self.val//self.paper_1
        count_paper_2 = (self.val-self.paper_1*count_paper_1)//self.paper_2
        count_coin_1 = (self.val-self.paper_1*count_paper_1-self.paper_2*count_paper_2)//self.coin_1
        count_coin_2 = (self.val-self.paper_1*count_paper_1-self.paper_2*count_paper_2-self.coin_1*count_coin_1)//self.coin_2
        print(f"""{self.paper_1}원 지폐는 {count_paper_1}개
            {self.paper_2}원 지폐는 {count_paper_2}개
            {self.coin_1}원 동전은 {count_coin_1}개
            {self.coin_2}원 동전은 {count_coin_2}개 입니다.""")    

A = auto_cal(52520, 10000, 1000, 100, 10)
auto_cal.Calculation(A)

#가격이 val인 물건을 살때 필요한 지폐, 동전의 수(10000원, 1000원, 100원 ,10원)
class auto_cal:
    def __init__(self, val, paper_1, paper_2, coin_1, coin_2):
        self.val = val
        self.paper_1 = paper_1
        self.paper_2 = paper_2
        self.coin_1 = coin_1
        self.coin_2 = coin_2

    def Calculation(self):
        count_paper_1 = self.val//self.paper_1
        count_paper_2 = (self.val-self.paper_1count_paper_1)//self.paper_2
        count_coin_1 = (self.val-self.paper_1count_paper_1-self.paper_2count_paper_2)//self.coin_1
        count_coin_2 = (self.val-self.paper_1count_paper_1-self.paper_2count_paper_2-self.coin_1count_coin_1)//self.coin_2
        print(f"""{self.paper_1}원 지폐는 {count_paper_1}개
            {self.paper_2}원 지폐는 {count_paper_2}개
            {self.coin_1}원 동전은 {count_coin_1}개
            {self.coin_2}원 동전은 {count_coin_2}개 입니다.""")

A = auto_cal(52520, 10000, 1000, 100, 10)
auto_cal.Calculation(A)