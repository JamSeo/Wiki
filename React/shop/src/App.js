import axios from 'axios'
import { lazy, Suspense, createContext, useEffect, useState } from 'react';
import { Routes, Route, useNavigate, Outlet } from 'react-router-dom'
import { useQuery } from 'react-query';
import { Nav, Navbar, Container, Row, Col, Button } from 'react-bootstrap'

import './App.css';
import data from './data'

// import Detail from './routes/Detail.js'
// import Cart from './routes/Cart.js'
const Detail = lazy(()=>import('./routes/Detail.js'))  // lazy 로딩으로 당장 필요없는 Component 늦게 렌더링
const Cart = lazy(()=>import('./routes/Cart.js'))

let 재고 = [11, 12, 14]
export let Context1 = createContext()  // state 보관함

function App() {

  // localStorage에 data 삽입
  let obj = {name: 'kim'}
  localStorage.setItem('data', JSON.stringify(obj))
  // localStorage에서 data 꺼내기
  let 꺼낸거 = localStorage.getItem('data')
  console.log(JSON.parse(꺼낸거).name)

  useEffect(()=>{
    if (!localStorage.getItem('visited')) {
      localStorage.setItem('visited', JSON.stringify([]))
    }
  })

  let [shoes, setShoes] = useState(data)
  let navigate = useNavigate()

  // React-Query 요청
  let result = useQuery('작명', ()=>
    axios.get('https://codingapple1.github.io/userdata.json')
    .then((res)=>res.data),
    { staleTime : 2000 }
  )
  console.log(result)

  return (
    <div className="App">
      {/* Navbar */}
      <Navbar bg="black" data-bs-theme="dark">
        <Container>
          <Navbar.Brand onClick={()=>{ navigate('/') }}>29cm</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link onClick={()=>{ navigate('/') }}>Home</Nav.Link>
            <Nav.Link onClick={()=>{ navigate('/cart') }}>Cart</Nav.Link>
          </Nav>
          <Nav>
            <div style={{ color: 'white' }}>
              { result.isLoading && '로딩중' }
              { result.error && '에러남' }
              { result.data && result.data.name }
            </div>
          </Nav>
        </Container>
      </Navbar>
      {/* Routes 목록 */}
      <Routes>
        <Route path='/' element={<Main shoes={shoes} setShoes={setShoes}/>} />
        <Route path='/detail/:id' element={
          // <Suspense fallback={<div>로딩중임</div>}>
          <Context1.Provider value={{ 재고 }}>
            <Detail shoes={shoes} 재고={재고} />
          </Context1.Provider>
            // </Suspense>
        } />
        <Route path='/cart' element={<Cart />} />

        {/* <Route path='/about' element={<About/>}>
          <Route path='member' element={<div>멤버임</div>} />
          <Route path='location' element={<div>위치정보임</div>} />
        </Route>
        <Route path='*' element={<div>없는 페이지입니다...</div>} /> */}
      </Routes>
    </div>
  )
}

function Main(props) {

  let shoes = props.shoes
  let [count, setCount] = useState(2)

  return (
    <>
      {/* 대문 */}
      <div className='main-bg'></div>
      <br />
      {/* 정렬버튼 */}
      <Button variant="secondary" size="sm" onClick={()=>{
        let copy = [...shoes]
        copy.sort(function(a, b) {
          let titleA = a.title.toUpperCase()
          let titleB = b.title.toUpperCase()
          if (titleA < titleB) {
            return -1
          }
          if (titleA > titleB) {
            return 1
          }
          return 0 
        })
        props.setShoes(copy)
      }}>정렬</Button>
      <br />
      {/* 상품 */}
      <Container>
        <Row>
          {
            shoes.map(function(shoe) {
              return <Card shoe={shoe} />
            })
          }
        </Row>
      </Container>
      <br />
      {/* 더보기 버튼 */}
      <Button size="sm" onClick={()=>{ 

        setCount(count + 1)

        // 동시에 ajax 여러개 요청하기
        // Promsise.all([ axios.get('/url1'), axios.get('/url2') ])
        axios.get(`https://codingapple1.github.io/shop/data${count}.json`)
        .then((res)=>{ 
          let copy = [...shoes, ...res.data]
          props.setShoes(copy)
         })
         .catch(()=>{ alert("상품이 더 없습니다.") })
       }}>더보기</Button>
    </>
  )
}

// function About() {
//   return (
//     <div>
//       <h4>회사정보임</h4>
//       <Outlet></Outlet>
//     </div>
//   )
// }

function Card(props) {

  let navigate = useNavigate()

  return (
    <Col sm={4} className='item' onClick={()=>{navigate(`/detail/${props.shoe.id}`)}}>
      <img src={"https://codingapple1.github.io/shop/shoes" + (props.shoe.id+1) + ".jpg"} width="100%" alt="" />
      <h5>{ props.shoe.title }</h5>
      <p>₩{ props.shoe.price }</p>
    </Col>
  );
};


export default App;