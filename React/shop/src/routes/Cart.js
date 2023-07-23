import { useMemo, memo, useState } from 'react'
import { Table } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import { addCount, subCount, removeCart } from './../store/cartSlice.js'

let Child = memo(function() {  // memo: 꼭 필요할때만 렌더링 해줘~
  console.log('재렌더링 됨')    // props 값이 변할 때만 렌더링됨
  return <div>자식임</div>      // props가 길고 복잡하면 손해임...
})                              // 꼭 필요한 무거운 Component에만 사용

function 함수() {
  return 
}


function Cart() {

  let result = useMemo(()=>함수(), [])  // Cart 컴포넌티 렌더링 시 1회만 실행됨, state가 변할때만 실행
  let cart = useSelector((state)=>state.cart)
  let [count, setCount] = useState(0)

  return (
    <div>
      <Child count={count} />
      <button onClick={()=>{ setCount(count + 1) }}>+</button>

      <Table striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>변경하기</th>
            <th>삭제</th>
          </tr>
        </thead>
        <tbody>
          {
            cart.map((item, i)=>{
              return <TableBody item={item} i={i} />
            })
          }
        </tbody>
      </Table>
    </div>
  )
}

export default Cart


function TableBody({item, i}) {

  let dispatch = useDispatch()
  let cart = item
  let idx = i + 1

  return (
    <tr>
      <td>{ idx }</td>
      <td>{ cart.name }</td>
      <td>{ cart.count }</td>
      <td>
        <button onClick={()=>{ dispatch(addCount(cart.id)) }}>+</button>
        <button onClick={()=>{ dispatch(subCount(cart.id)) }}>-</button>
      </td>
      <td><button onClick={()=>{ dispatch(removeCart(cart.id)) }}>삭제</button></td>
    </tr> 
  )
}

