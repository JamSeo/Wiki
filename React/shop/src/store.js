import { configureStore } from '@reduxjs/toolkit'
import cart from './store/cartSlice.js'


export default configureStore({
  reducer: { 
    cart: cart.reducer,
  }
})  