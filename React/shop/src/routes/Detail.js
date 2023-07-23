import { useContext, useEffect, useState } from 'react'
import { useParams } from "react-router-dom"
import { useDispatch } from 'react-redux'
import { addToCart } from './../store/cartSlice.js'
import { Nav } from 'react-bootstrap'
import { Context1 } from '../App.js'


function Detail(props) {

  let dispatch = useDispatch()
  let { id } = useParams()
  let idx = parseInt(id)
  let shoe = props.shoes.find((shoe)=>shoe.id === idx)
  let [eventTag, setEventTag] = useState(true)
  let [tab, setTab] = useState(0)
  let [fade2, setFade2] = useState('')

  useEffect(()=>{
    let a = setTimeout(()=>{ setFade2('end') }, 100)
    return ()=>{
      clearTimeout(a)
      setFade2('')
    } 
  }, [])

  useEffect(()=>{
    let a = setTimeout(()=>{ setEventTag(false) }, 2000)
    return ()=>{
      clearTimeout(a)  // 기존 데이터 요청은 제거해주세요~
    }
  }, []) 

  useEffect(()=>{
    let data = localStorage.getItem('visited')
    data = JSON.parse(data)
    data.unshift(shoe.title)
    data = new Set(data)
    data = Array.from(data)
    localStorage.setItem('visited', JSON.stringify(data))
  }, [])


  return (
    <div className={'container start '  + fade2}>     

      { 
        eventTag === true
        && <div className="alert alert-warning">2초 이내 구매시 할인</div>
      } 

      <div className="row">
        <div className="col-md-6">
          <img src={"https://codingapple1.github.io/shop/shoes" + (idx+1) + ".jpg"} alt="" width="100%" />
        </div>
        <div className="col-md-6">
          <h4 className="pt-5">{ shoe.title }</h4>
          <p>{ shoe.content }</p>
          <p>{ shoe.price }원</p>
          <button className="btn btn-danger" onClick={()=>{ 
            dispatch(addToCart({id: shoe.id, name: shoe.title, count: 1}))
            alert("장바구니에 상품이 추가되었습니다.")
          }}>주문하기</button> 
        </div>
      </div>

      <Nav variant="tabs" defaultActiveKey="link0">
        <Nav.Item>
          <Nav.Link onClick={()=>{ setTab(0) }} eventKey="link0">버튼1</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link onClick={()=>{ setTab(1) }} eventKey="link1">버튼2</Nav.Link>
        </Nav.Item>
        <Nav.Item>
          <Nav.Link onClick={()=>{ setTab(2) }} eventKey="link2">버튼3</Nav.Link>
        </Nav.Item>
      </Nav>
      <TabContent tab={tab} shoes={props.shoes} />
    </div> 
  )
}

function TabContent({tab, shoes}) {

  let [fade, setFade] = useState('')

  useEffect(()=>{
    let a = setTimeout(()=>{ setFade('end') }, 100)

    return ()=>{
      clearTimeout(a)
      setFade('')
    } 
  }, [tab])

  return (<div className={'start ' + fade}>
    { [<div>{ shoes[0].title }</div>, <div>내용2</div>, <div>내용3</div>][tab] }
  </div>)
}

export default Detail;