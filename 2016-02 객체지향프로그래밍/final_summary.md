2016-2 OOP 기말대비
===================

----------


상속(Inheritance)
--------------

#### 상속이란

+ class A extends B
+ 부모 클래스의 모든 메소드를 다시 구현하는 것없이 사용하는 것
+ 필드와 메소드가 상속된다.

#### 상속의 장점

+ 중복된 코드 제거
+ 유지보수
+ 자식 클래스를 빠르게 구성 가능
+ 다형성

#### 어떻게
+ (ACCESS_MODIFIER) (CLASS_NAME) extends (PARENT_CLASS_NAME) {...}
+ 다중 상속 불가



---

다형성(Polymorphism)
--------------

#### 설명할 수 있는 가장 직관적인 코드

    class A{
        public String x(){return "A.x";}
    }
    class B extends A{
        public String x(){return "B.x";}
        public String y(){return "y";}
    }
    class B2 extends A{
        public String x(){return "B2.x";}
    }
    public class PolymorphismDemo1 {
        public static void main(String[] args) {
            A obj = new B();
            A obj2 = new B2();
            System.out.println(obj.x());
            System.out.println(obj2.x());
        }
    }

이 코드를 실행하면 실행결과는 **B.x, B2.x** 이다.

#### 한문장으로?

다형성이란 "여러 종류의 오브젝트를 하나의 오브젝트(by Type Casting)로 사용하는 것?"


#### 장점
+ 유지보수
+ 각각의 오브젝트 모듈화 가능

#### 참고 사이트
[생활코딩: 다형성](https://opentutorials.org/module/516/6127)

-----


오브젝트와 클래스
--------------

+ 클래스: field(속성 정의), method(함수 정의)
+ 인스턴스: 클래스로 부터 만들어진 오브젝트, 하나의 클래스로부터 여러 인스턴스 생성 가능, "new" 키워드로 만들기

-----


OOP 프로그램 개발 절차 
--------------
1. 클래스 디자인
2. 클래스로 부터 인스턴스 생성
3. 인스턴스(클래스로 부터 만들어진 오브젝트) 사용
4. We will cover how to create a class (개어려워 ㅇㅅㅇ)


-----

클래스 implementation
--------------
#### 클래스의 이름 결정
+ 영어 사용 권장(첫번째 글자는 숫자 불가/ $, _ 제외하고는 특수문자 사용불가 / int, while 같은 java keyword 사용 불가)
+ 관습: 첫번째 글자는 대문자

#### 클래스의 정의
+ 한 파일에 한 최상위 클래스
+ (access modifier) class (class_name) {...}
+ 파일 이름: (class_name).java

-----

클래스의 구성
--------------

#### Constructor
+ 클래스가 "선언"될 때(new 키워드가 호출될 때) 한번 호출됨 (클래스 생성자)
+ 필드 값 초기화, 다른 객체 생성을 위한 메소드 호출에 사용됨
+ Constructor가 정상적으로 실행되면 객체는 Heap에 생성되고, 이의 주소값이 Stack에 저장됨
+ 기본 Constructor가 존재. 별도 선언 안해도 됨.

#### Field
+ 클래스의 데이터 보관 (클래스 내 변수)
+ 변수 선언 처럼 선언하면 됨. Constructor나 Method안에 선언하면 안됨.
+ (instance_name).(field_name) 으로 접근

#### Method
+ 클래스의 행동 정의 (클래스 내 함수)
+ Return Type, Method Name, Arguments, Code body로 구성
+ Method의 이름 결정: Class 이름 결정과 같은 규칙이나, 관례적으로 소문자를 주로 사용하고, [카멜 표기법](https://namu.wiki/w/%EC%BD%94%EB%94%A9%20%EC%8A%A4%ED%83%80%EC%9D%BC#s-3)을 따른다.

-----

클래스 내/외부에서의 Method 호출 차이
--------------
#### 외부에서 호출하기
    Calculator calc = new Calculator();
    int[] numbers = {10,9,8,7,6};
    System.out.println(calc.average(numbers));

#### 내부에서 호출하기
    double divide(int x, int y) {
        double result = (double) x / (double) y;
        return result;
    }
    
    public static void main(String[] args) {
       int sum = divide(10,20);
    }

-----

Overloading
--------------
#### What
같은 이름으로 다른 인자값, 타입으로 함수를 정의할 수 있다.

    int plus(int x, int y) {
        return x + y;
    }
    
    double plus(double x, int y) {
        return x + y;
    }
    
    int plus(int x) {
        return x + 10;
    }
    
    public void main() {
        int sum1 = plus(1+2);
        double sum2 = plus(2.3, 4.5);
        int sum3 = plus(10);
    }    
    
#### Why
유사한 기능으로 다른 인자값이나 다른 타입 형태로 메서드를 만들고 싶을 때 유용하다.


#### Attention
+ 인자의 Type, 인자의 개수, 인자의 순서 중 하나는 반드시 달라야 한다.
+ Return Type은 관계 없다.
+ System.out.println()이 Overloading의 좋은 예


-----

메모리 영역
--------------
![메모리 영역 구조도](http://www.pointsoftware.ch/wp-content/uploads/2012/11/Cookbook_JVMArguments_3_MemoryModel.png)

#### Stack
원시형 변수를 저장, 그 외의 참조형 변수(Reference Type), 동적 변수(Dynamic Type) 등은 주소값만 저장

#### Heap
Stack에서 관리 가능한 데이터를 제외한 데이터를 저장하기 위한 공간

-----

this 키워드
--------------
#### 의미
인스턴스 자신을 가리킬 때 사용됨

#### 사용 예시
    
    public class Person {
        String name;
        int age;
    
        Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
        
        void talk(String says) {
            System.out.println(says);
        }
    }

-----

static 키워드
--------------

#### 의미
변경되지 않음, dynamic(동적)의 반의어

#### Static Member vs Instance Member
##### 메모리 영역
Instance Member는 Heap 영역에, Static Member는 Method 영역에 저장됨

##### 접근법
Instance Member는 클래스로 부터 객체(인스턴스) 생성 후 접근해야하지만, Static Member는 바로 사용가능

##### When What?
객체 별로 다른 값을 가져야 할 시 Instance Member, 고정된 값을 가질 시 Static Member


#### How to Use
```
public class StaticMember {
    String color;
    static double pi = 3.14159;
    (...)
}

StaticMember staticExcercise = new StaticMember();
double sizeOfCircle = StaticMember.pi * radius * radius; //권장
sizeOfCircle = staticExcercise.pi * radius * radius; //ㄴㄴ
```

#### 주의사항
+ Static Method안에서 Instance Member 사용 불가

#### 필요성
+ 메모리 효율성 (Static Member는 한번만 생성됨) = 가능할 시 static 사용 권장
+ Instance Member를 사용하지 않는 Method임을 인지 가능

-----

Java 패키지
--------------

#### 왜
보통 우리가 여러 파일들을 폴더 단위로 관리하는 것 처럼 우리는 패캐지를 사용하여 여러 클래스를 패키지 안에 담아서 관리 한다.


#### 어떻게
디렉토리가 계층 구조로 관리되는 것 처럼, 패키지도 계층 구조로 관리된다.


Access modifier
--------------

![Access Modifier](http://1.bp.blogspot.com/-4Q4ijZ2xEYs/VfUZBPAZMdI/AAAAAAAAB2o/cloTxt6oLSQ/s1600/java-member-access-levels1.png)

#### public
- 다른 객체에서 모든 field/Method 접근이 가능하다.

HousePark.java
```
public class HousePark {
    protected String lastname = "park";
    public String info = "this is public message.";
}

```
EungYongPark.java
```
public class EungYongPark extends HousePark {
    public static void main(String[] args) {
        EungYongPark eyp = new EungYongPark();
        System.out.println(eyp.info); // this is public message
    }
}

```

#### protected
+ 같은 패키지 내에서만 접근이 가능하다
+ 다른 패키지지만 자식 클래스라면 접근이 가능하다.

HousePark.java (in house package)
```
package house;
public class HousePark {
    protected String lastname = "park";
}
```
EungYongPark.java (in person package)
```
package person;

import house.HousePark;

public class EungYongPark extends HousePark {       
    public static void main(String[] args) {
        EungYongPark eyp = new EungYongPark();
        System.out.println(eyp.lastname); // park 출력
        
        HousePark s = new HousePark();
        System.out.println(s.lastname); // 이렇게 접근하면 안됨
    }    
}
```

#### private
- 다른 외부 객체에서 접근할 수 없다.
- Ruby 클래스 내에서만 getSecret 함수를 실행시킬 수 있다.
```
public class Ruby {
    String abs;
    private void getSecret() {
        System.out.println(this.abs);
    }
    public static void main(String[] args) {
        Ruby s = new Ruby();
        s.getSecret();
    }
}

```

#### default
- 다른 패키지에서 접근할 수 없다. 

HouseKim.java
```
package house;

public class HouseKim {
    String lastname = "kim"; // default access modifier
}
```
HousePark.java
```
package house;

public class HousePark {
    String lastname = "park";

    public static void main(String[] args) {
        HouseKim kim = new HouseKim();
        System.out.println(kim.lastname);
    }
}

```

#### When getter/setter is useful
- 필드 값의 무결성 보장
- 사람이라는 객체에서 age 라는 맴버 변수가 있고 다른 관계 없는 객체에서 age(나이) 값을 음수로 변경하려는 그런 시나리오를 피할 수 있음

-----

final 키워드
--------------

#### What

해당 field의 마지막 값임을 의미

#### When

반드시 Constructor 안에서 또는 선언할 때 사용되어야 한다.


#### Why

값을 변경하지 못하도록 하기 위함


#### final class & final method
+ final class는 상속 불가, 예측되지 않은 상황을 방어하는 수단
+ final method는 override 불가


-----


super()
--------------
+ dmb cellphone 은 dmb 채널이 몇개까지 가능하고 dmb 채널에 가입되어있는지 인자값을 받는다.
+ Cellphone 은 제조사와 통신사를 생성자로 받는다.

CellPhone.java
```
public class CellPhone {
    String manufactural;
    String commoncarrier;

    public static String info = "cellphone object";

    public CellPhone(String manufactural, String commoncarrier) {
        this.manufactural = manufactural;
        this.commoncarrier = commoncarrier;
    }
}
```
+ DmbCellPhone 에서 CellPhone을 상속 받아서 기본적인 사항(제조사, 통신사) 를 받아서 부모 클래스 생성자를 DmbCellPhone 생성자에서 실행 시킨다.

DmbCellPhone.java

```
public class DmbCellPhone extends CellPhone {
    int dmbChannelCount;
    boolean dmbRegistered;

    public DmbCellPhone(String manufactural, String commoncarrier , int dmbChannelCount, boolean register) {
        super(manufactural, commoncarrier);
        this.dmbChannelCount = dmbChannelCount;
        this.dmbRegistered = register;
    }

}


```

-----

Overriding
--------------

#### What
부모로 부터 상속받은 Method를 rewrite 하는 것.

#### Attention
+ Signature(Return Type, Method name, Arguments)는 부모와 같아야 한다.
+ Access modifier가 부모보다 강하게 설정될 수 없다.
+ @Override를 이용해 Override 한다.
```
class Parent {
    void method1() {...}
    void method2() {System.out.println("Parent2");}
}

class Child extends Parent {
    @Override
    void method2() {System.out.println("Child2");}
    void method3() {
        method2();
        super.method2();
    }
}
```
위의 Child class의 method3 실행결과는 **Child2, Parent2**임을 숙지.


#### Annotation
Annotation(@)은 method나 field의 meta data(컨텍스트 정보)를 제공한다.

#### Override vs Overload
Overload는 같은 이름으로 새로운 method 정의를 하는 것 (arguments는 다르게)이지만 Override는 이미 부모에서 정의된 method를 재정의하는 것.

-----


Type Casting (다형성과 상속 결합)
--------------

![Class Type Casting](http://i.imgur.com/84EUxPO.png)

*Direct Child만 Parent로 Type casting 가능*

+ 최상위 부모에서 자식을 TypeCasting

Human.java
```
public class Human {

}
```
Gabrial.java
```
public class Gabrial extends Human {

}
```

Main.java
```
public class Main {
    Human s = new Gabrial();
}
```

+ 부모 (최상위가 아닌) 클래스에서 자식을 Typecasting

GabrialSon.java (가브리엘의 아들)
```
public class GabrialSon extends Gabrial {

}
```
Main.java
```
public class Main {
    public static void main (String [] args) {
        Human s = new Gabrial();
        Gabrial b = new GabrialSon(); // Type cast 가능

    }
}
```


-----

instanceof 함수
--------------

* Type Casting 가능한지 확인 하는 함수
* a instanceof B가 True라면 a는 B로 Type Casting 가능

-----

추상화(Abstraction)
--------------
#### What
+ **추상화**란 특정 상황에서 일반적인 규칙, 개념 다시 말해 규격화하는 프로세스이다.
+ **OOP에서 추상화**란 세부사항을 일부 숨기고, 공통적이며 필수적인 기능을 보여주는 것을 의미한다.
+ Example with Person
    - 사람은 어린이, 학생, 친구, 파트타임 직원일 수 있다.
    - 여기서 사람을 표현하는 데 사용된 공통된 특성은 "직업" 또는 "역할"

#### For
- OOP에서 추상화의 목표는 객체를 일반화하여 재사용하기 용이하게 만드는 것이다.


```
abstract class Calculator{
    int left, right;
    public void setOprands(int left, int right){
        this.left = left;
        this.right = right;
    } 
    int _sum() {
        return this.left + this.right;
    }
    public abstract void sum();  
    public abstract void avg();
    public void run(){
        sum();
        avg();
    }
}
class CalculatorDecoPlus extends Calculator {
    public void sum(){
        System.out.println("+ sum :"+_sum());
    }
    public void avg(){
        System.out.println("+ avg :"+(this.left+this.right)/2);
    }
} 
class CalculatorDecoMinus extends Calculator {
    public void sum(){
        System.out.println("- sum :"+_sum());
    }
    public void avg(){
        System.out.println("- avg :"+(this.left+this.right)/2);
    }
} 
public class CalculatorDemo {
    public static void main(String[] args) { 
        Calculator c1 = new CalculatorDecoPlus();
        c1.setOprands(10, 20);
        c1.run();
         
        Calculator c2 = new CalculatorDecoMinus();
        c2.setOprands(10, 20);
        c2.run();
    }
   
}
```

-----

추상 Class
--------------

#### What
여러 Class의 공통 기능 등을 규격화 하는 Class

#### Why
특정 메소드를 반드시 Override해서 구현하도록 강요 = 규격화

#### How
(ACCESS_MODIFIER) abstract class (CLASS_NAME)



Interface
--------------

#### Why
무엇을 구현해야하는 지 정의
객체 사용 방법 정의
다형성 강화

#### vs Abstract Class

- interface 는 함수 선언만 가능하다.
```
public interface ChatInterface {
    public void helpMe(String myJob);
}
```
- Abstract 는 함수 선언과 구현(implements)이 모두 가능하다
```
public abstract static class Overwatch implements ChatInterface {
    public abstract String myCharacter();
    public abstract void ultimate();
    
    public void defaultAttack() {
        System.out.println("Damage +25");
    }
}
```




Mix of 추상, 인터페이스
--------------

```
public interface ChatInterface {
    public void helpMe(String myJob);
}

public abstract static class Overwatch implements ChatInterface {
    public abstract String myCharacter();
    public abstract void ultimate();
    public void defaultAttack() {
        System.out.println("Damage +25");
    }
}

public static class Mei extends Overwatch {
    @Override
    public String myCharacter() {
        return "Scientist";
    }

    @Override
    public void ultimate() {
        System.out.println("똥주 뿌시쪄우!");
    }

    @Override
    public void helpMe(String myJob) {
        System.out.println(myJob+"가 도와달라고 합니다!");
    }
}

public static class Soldier76 extends Overwatch {
    @Override
    public String myCharacter() {
        return "Soldier";
    }

    @Override
    public void ultimate() {
        System.out.println("목표를 포착했다!");
    }

    @Override
    public void helpMe(String myJob) {
        System.out.println(myJob+"가 도와달라고 합니다!");
    }
}

public static void main(String[] args){
    Overwatch rainc = new Mei();
    Overwatch renov = new Soldier76();
    rainc.ultimate();
    renov.helpMe(renov.myCharacter());
    renov.defaultAttack();
}
```

try-catch-finally
--------------
+ 실행도중에 발생되는 RuntimeException을 Handling
```
try{
    파일 열기
    파일 읽기 및 처리
} catch (IOException e){
    파일 입출력 처리
} catch (OtherException|OtherException2 e){
    다른 오류 처리
} finally {
    파일 닫기
}
```
+ Custom Exception
```
public static void main(String[] args){
    try{
        PlayNumber player = new PlayNumber();
        player.printNumber(-1);
    } catch (PlayNumber.MinusException e) {
        e.printStackTrace();
    }
}

public static class PlayNumber{
    public void printNumber(int num) throws MinusException {
        if (num < 0) throw new MinusException();
        else System.out.println(String.format("%d", num));
    }

    public class MinusException extends Exception{
        @Override
        public String getMessage() {
            return "You cannot put minus value";
        }
    }
}
```

Collection framework
--------------
*어떻게 사용하는지 숙지*

+ List
    - ArrayList, LinkedList 
    - 같은 element 가 들어가도 괜찮음
    - insertion 할 때 order 가 되도록 저장 가능
    
+ Map
    + Key-value 저장 타입
    + Key가 겹치면 안됨
    + Hashmap, TreeMap

+ List Functions
![List Functions](http://i.imgur.com/W14uiAV.png)

```
public class ListExample {
    private List<String> slackIds = new ArrayList<String>();

    public ListExample() {
        slackIds = new LinkedList<String>();
        slackIds.add("leeky");
        slackIds.add("1g");
        slackIds.add("20132368");
    }

    public void iterateIds() {
        for (String id : slackIds) {
            System.out.println(id);
        }

        System.out.println(slackIds.get(1));
        slackIds.remove(1);
        System.out.println(slackIds.size());
        System.out.println(slackIds.get(1));
        slackIds.add("20163080");
        System.out.println(slackIds.size());
    }
}
```