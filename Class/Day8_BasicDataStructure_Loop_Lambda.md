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
>  \t가 ,로 변환됨
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

***

### 3. Lambda
#### palindrome algorithm
> 특정 문자열과 reverse한 문자열을 비교하여 같은 값이 나오면 True, 다른 값이 나오면 False를 반환
> ```python
> def is_pal(string):
>     rev=string[::-1]
>     if rev == string:
>         return True
>     else:
>         return False
> ```
> Lambda로 표현하면 다음과 같다
> ```python
> is_pal=lambda string : string == string[::-1]
> ```

#### csv Function
> seperate값을 다르게 주고 싶은 상황이 발생<br>
> e.g. > :, ::, |, ...
> ```python
> # read_csv function이 정의되어 있고, filename과 sep를 parameter로 받는 경우
> seps=[",", ":", "::", "|"]
> reader={};
> for sep in seps:
>     reader[sep]=lambda filename: read_csv(filename, sep);
> # | 로 구분된 파일을 처리하는 경우
> reader["|"](test.txt)
> ```

***

### 4. python 개발환경 구축
#### pyenv(언어에 대한 버전 관리)
>- 설치 : [link](https://github.com/yyuu/pyenv-installer)
>- 참고 : [link](https://github.com/yyuu/pyenv/wiki/Common-build-problems)
>- pyenv shell [version]으로 버전 변경 가능(프로젝트 및 설치 패키지 변경은 불가능)

#### virtualenv(프로젝트에 대한 버전 관리)
>- pyenv 설치 시 자동 설치 됨
>- pyenv virtualenv [version] [projectName] 으로 project 버전 생성
>- pyenv activate [projecName]으로 project 활성화
>- pyenv deactivate [projectName]으로 projec 비활성화

#### autoenv(자동 activate)
>- 특정 디렉토리 진입 시 자동 activate
>- 프로젝트 디렉토리에 .env파일을 만들고 pyenv activate [projectName]구문을 추가
>- DB패스워드 등을 포함시켜도 괜찮으나, gitignore에 반드시 포함 시켜야 함