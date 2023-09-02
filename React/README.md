# React

## React-Router

1. 설치 코드  
   ![](./img/캡처1.PNG)

2. index.js  
   ![](./img/캡처2.PNG)

3. App.js  
   ![](./img/캡처3.PNG)

4. 구현모습  
   ![](./img/캡처4.PNG)

5. Link 구현  
   ![](./img/캡처5.PNG)

6. useNavigate 구현  
   ![](./img/캡처6.PNG)

<br />

## styled-components

### styled-components 장점

- CSS 파일 안열어도 됨
- 스타일이 다른 js 파일로 오염되지 않음
- 페이지 로딩시간 단축

### styled-components 구현

1. 설치 코드  
   ![](./img/styled-components1.JPG)

2. js 파일  
   ![](./img/styled-components2.JPG)

3. 구현모습  
   ![](./img/styled-components3.JPG)

4. js 파일에 CSS 파일 종속시키는 또다른 방법  
   ![](./img/styled-components4.JPG)

5. props를 활용한 구현  
   ![](./img/styled-components5.JPG)

<br />

## react-query

(업데이트 사항) 라이브러리 이름이 react-query에서 @tanstack/react-query로 바뀌어서

```
npm install @tanstack/react-query
```

1. 설치시엔 이거 입력합시다

```javascript
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from "@tanstack/react-query";
```

2. import 해서 사용시엔 이거 입력합시다

```javascript
useQuery(['작명'],
```

3. useQuery쓸 때 '작명' 말고 ['작명'] 입니다

<br />
 
ajax 요청하다보면 이런 기능들이 가끔 필요해집니다.

- 몇초마다 자동으로 데이터 다시 가져오게 하려면?

- 요청실패시 몇초 간격으로 재시도?

- 다음 페이지 미리가져오기?

- ajax 성공/실패시 각각 다른 html을 보여주려면?

직접 개발해도 되겠지만 귀찮으면 react-query 라는 라이브러리 설치해서 써도 됩니다.

SNS, 코인거래소같은 실시간 데이터를 보여줘야하는 사이트들이 쓰면 유용하고

나머지 사이트들은 딱히 쓸데는 없습니다.

원래 강의할 때 다양한거 얕게 찍먹하면 "와 많은걸 배웠네요" 하면서 만족도가 높아지는 이상한 현상이 있습니다.

그래서 찍먹하고 넘어가야합니다.

### react-query 설치 & 셋팅은

터미널에서 npm install react-query 하고

index.js 파일 열어서

```javascript
import { QueryClient, QueryClientProvider } from "react-query"; //1번
const queryClient = new QueryClient(); //2번

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <QueryClientProvider client={queryClient}>
    {" "}
    //3번
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </QueryClientProvider>
);
```

1번 2번 3번 하면 됩니다.

### react-query로 ajax 요청하는 법

그냥 ajax 요청해도 되는데

react-query를 써서 ajax 요청을 날리면 더 편리한 기능을 제공합니다.

```javascript
function App() {
  let result = useQuery("작명", () =>
    axios.get("https://codingapple1.github.io/userdata.json").then((a) => {
      return a.data;
    })
  );
}
```

useQuery 라는걸 상단에서 import 해온 뒤에

useQuery()로 ajax 요청을 감싸면 됩니다.

그럼 유용한 기능을 제공해주는데

### 장점1. ajax 요청 성공/실패/로딩중 상태를 쉽게 파악할 수 있습니다.

```javascript
function App() {
  let result = useQuery("작명", () =>
    axios.get("https://codingapple1.github.io/userdata.json").then((a) => {
      return a.data;
    })
  );

  return (
    <div>
      {result.isLoading && "로딩중"}
      {result.error && "에러남"}
      {result.data && result.data.name}
    </div>
  );
}
```

result라는 변수에 ajax 현재 상태가 알아서 저장됩니다.

- ajax요청이 로딩중일 땐 result.isLoading 이 true가 됩니다.

- ajax요청이 실패시엔 result.error 가 true가 됩니다.

- ajax요청이 성공시엔 result.data 안에 데이터가 들어옵니다.

그래서

ajax 로딩중일 땐 `<A/>` 보여주세요~

ajax 성공시엔 `<B/>` 보여주세요~

이런거 직접 개발하려면 state 부터 만들어야 했을텐데 얘는 그럴 필요가 없습니다.

### 장점2. 틈만나면 알아서 ajax 재요청해줍니다.

페이지 체류하고나서 일정시간이 경과하거나

님들이 다른 창으로 갔다가 다시 페이지로 돌아오거나

다시 메인페이지로 돌아가거나

이런 여러 경우에 알아서 ajax 요청을 다시 해줍니다.

당연히 재요청 끄는 법, 재요청간격 조절하는 법도 있습니다.

### 장점3. 실패시 재시도 알아서 해줌

잠깐 인터넷이 끊겼거나 서버가 죽었거나 그러면 ajax 요청이 실패합니다.

실패했을 때는 얘가 4번인가 5번인가 재시도를 알아서 해줍니다.

편리합니다.

### 장점4. ajax로 가져온 결과는 state 공유 필요없음

지금 App 컴포넌트에서 유저이름 가져오는 ajax 요청을 날리고 있습니다.

근데 그 유저이름 결과가 Detail 컴포넌트에도 필요하면 어쩌죠?

- 유저이름을 props 전송하면 됩니다.

근데 실은 props 전송 필요없습니다.

Detail 컴포넌트에다가 유저이름 ajax 요청하는 코드 똑같이 또 적으면 됩니다.

react-query는 스마트하기 때문에 ajax 요청이 2개나 있으면 1개만 날려주고

캐싱기능이 있기 때문에 이미 같은 ajax 요청을 한 적이 있으면 그걸 우선 가져와서 씁니다.

react-query가 주장하는 장점은

server-state (DB 데이터)를 프론트엔드에서 실시간 동기화해주는걸 도와준다고 합니다.

근데 ajax 요청을 몇초마다 계속 날려서 가져오는 방식이라 좀 비효율적일 수도 있습니다.

실시간으로 서버에서 데이터를 자주 보내려면 웹소켓이나 Server-sent events 같은 가벼운 방식들도 있습니다.

그래서 react-query는 ajax 관련 기능개발 편하게 할 수 있는데에 의의가 더 있습니다.

### RTK Query 라이브러리도 있음

Redux Toolkit 설치한 경우 RTK Query 라는것도 기본적으로 사용가능한데

비슷한 기능들을 제공합니다.

다만 셋팅하는 코드가 좀 더럽습니다.

RTK Query는 실은 다른 용도로도 많이 쓰는데

ajax 요청후 Redux state 변경을 하고 싶다면...

원래 Redux state변경함수 안에선 ajax요청하면 안되어서 컴포넌트 안에서 해야합니다.

근데 ajax 요청하는 코드가 다양하고 많으면 컴포넌트 안의 코드가 길어지고 관리도 귀찮은데

그런걸 Slice 안에서 관리가능하게 도와줍니다.

그리고 ajax 요청하는 코드가 100만개 있으면 그걸 편리하게 관리할 수 있게 도와줍니다.

근데 코드가 약간 더러울 뿐
