import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function App() {

  let [title, setTitle] = useState(['남자코트 추천', '강남 우동맛집', '파이썬 독학']);
  let [like, addLike] = useState([0, 0, 0]);
  let [modal, setModal] = useState(false);
  let [idx, setIdx] = useState(0)
  let [inputValue, setInputValue] = useState('')


  let [count, setCount] = useState(0);
  let [age, setAge] = useState(20);

  useEffect(()=>{
    if (count && count < 3) { setAge(age + 1) }
  }, [count])
  

  return (
    <div className="App">
      <div className="black-nav">
        <h4>ReactBlog</h4>
      </div>

      <div>
        <div>안녕하십니까 전 {age}</div>
        <button onClick={()=>{ setCount(count + 1) }}>누르면한살먹기</button>
      </div>

      {/* <button onClick={() => { 
        let copy = [...title]
        copy[0] = '여자코트 추천'
        commitTitle(copy)
      }}>버튼</button> */}

      {
        // 쇼핑 목록
        title.map(function(_, i){
          return (
            <div className="list" key={i}>
              <h4 onClick={() => { { setModal(!modal); setIdx(i) } }}>{title[i]}
                <span onClick={(e) => {
                  e.stopPropagation()
                  let copy = [...like]
                  copy[i] += 1
                  addLike(copy)
                }}>❤</span> {like[i]}
              </h4>
              <p>2월 17일 발행</p>
              <button onClick={()=>{
                let copy = [...title]
                copy.splice(i, 1)
                setTitle(copy)
              }}>삭제</button>
            </div>
          )
        })
      }

      {
        //input
        <div>
          <input onChange ={(e) => { setInputValue(e.target.value) }} />
          <button onClick={()=>{
            let copy = [...title]
            copy.unshift(inputValue)
            setTitle(copy)
          } }>제출</button>
        </div>
      }

      {
        // 모달창
        modal ? <Modal title={ title } idx={ idx }/> : null
      }
    </div>
  );
}


function Modal(props) { 
  return (
    <div className='modal'>
      <h4>{ props.title[props.idx] }</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}

export default App;