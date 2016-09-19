### 1. 기본내장 자료구조
#### List
>- 순서 존재, 중복 허용<br>
>- List를 multiLIne으로 선언 시 마지막에 ','를 붙여주는 것이 좋음<br>
> ㄴ git과 연관 있음<br>
>- indexing<br>
>    * [0:2]등으로 slicing하면 새로운 List가 반환됨
>    * [::-1]로 stride부분을 -1로 하면 reverse되어 출력

#### set
>- 순서 존재 X, 중복허용 없음

#### tuple
>- 순서 존재, 내부 값 변경 불가능
> ```python
> a, b=(100,200)
> ```
>- [이 아닌 (로 선언
>- Function의 return값을 정의할 때 사용

### dict
> ```python
> a={"name":"han"} << 이런 식으로 초기화
> ```
>- 초기화 후 값 추가는 a[keyName]=Value
>- key와 value에는 값이 중복되지 않음
> ```python
> for k, v in a.items():
>     print(k,v);
> ```
> 위의 방법으로 k, v를 출력할 수 있음

***

### 2. File I/O
#### with
> ```python
> with open("[fileName]", "[mode]") as fp:
>     data=fp.read();
> ```
> with를 이용해 자동 open / close가 가능함

#### String관련 함수
>-  split
>    * 특정 parameter로 나누어 list를 return 함
> ```python
> "dog,cat,fish".split(",")
> ```
> [dog, cat, fish]
>- join
>    * 특정 parameter를 매개로 문자열을 만들어 반환
>    * eval()과 함께 사용할 경우 쉽게 수식 계산이 가능함
> ```python
> ":".join([a, b, c])
> ```
> "a : b : c"
>- replace
>    * 특정 문자열을 replacing
> ```python
> data.replace("\t", ",")
> ```
> \t가 ,로 변환됨
>- format
>    * 출력시 %s, %d 등을 대체하는 기능
> ```python
> # regacy code
> "%s : hello !!" %(name);
> # formatting
> "{name} : hello!".format(name="han");
> #formatting 2
> "{name}, {mail}, {pNum}".format(name="han", mail="hkt@naver.com, pNum=01011111111")
> ```
