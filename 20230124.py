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
        count_paper_2 = (self.val%self.paper)//self.paper_2
        count_coin_1 = (self.val%count_paper_2)//self.coin_1
        count_coin_2 = (self.val%count_coin_1)//self.coin_2
        print(f"""{self.paper_1}원 지폐는 {count_paper_1}개
            {self.paper_2}원 지폐는 {count_paper_2}개
            {self.coin_1}원 동전은 {count_coin_1}개
            {self.coin_2}원 동전은 {count_coin_2}개 입니다.""")

A = auto_cal(52520, 10000, 1000, 100, 10)
auto_cal.Calculation(A)
