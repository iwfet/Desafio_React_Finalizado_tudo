import React from 'react'
import "./App.css"
import "./components/PostForm.css"
import PostForm from "./components/PostForm"

function App(){
  return(
    <div>
      <h1 className="title">Calculadora Salário Líquido</h1>
      <br />
      <h4 className="instruçoes">Para fazermos os calculos o mais preciso o possivel </h4>
      <h4 className="instruçoes">coloque ate os centavos com ponto</h4>
      <PostForm />
    </div>
  )
}
export default App;
