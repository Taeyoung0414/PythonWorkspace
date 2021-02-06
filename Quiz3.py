# Quiz : 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# ex) http://naver.com

# 조건1) http:// 부분은 제외 => naver.com
# 조건2) 처음 만나는 점(.) 이후 부분은 제외 => naver
# 조건3) 남은 글자 중 처음 세 자리(nav) + 글자 갯수(5) + 글자 내 'e'의 갯수(1) + "!" 로 구성

# = 생성된 비밀번호 : nav51!


# Answer
url = "http://naver.com"

opt1 = url.replace("http://", "")
print(opt1)

opt2 = opt1[:opt1.index(".")]
print(opt2)

pw = opt2[:4] + str(len(opt2)) + str(opt2.count("e")) + "!"

print(pw)