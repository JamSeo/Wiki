import { createSlice } from '@reduxjs/toolkit'

let cart = createSlice({
    name: 'cart',
    initialState: [
        {id: 2, name: 'Grey Yordan', count: 1},
        {id: 0, name: 'White and Black', count: 2},
    ],
    reducers: {
        addCount(state, action){
            let item = state.find((item)=>item.id === action.payload)
            item.count++
        },
        subCount(state, action){
            let item = state.find((item)=>item.id === action.payload)
            
            if (item.count) {
                item.count--
            }
        },
        addToCart(state, action){
            let item = state.find((item)=>item.id === action.payload.id)

            if ( item ) {
                item.count++
            } else {
                state.push(action.payload)
            }
        },
        removeCart(state, action){
            state.pop(action.payload)
        }
    }
})

export let { addCount, subCount, addToCart, removeCart } = cart.actions

export default cart