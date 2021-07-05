import React from 'react'
import api from '../api'


function PostForm () {  
    const [data, setData] = React.useState({
    
    });
    
    async function submit (e){
        e.preventDefault();
        const {salario_bruto,Descontos,Dependentes} = e.target
        console.log(salario_bruto.value)
        const dados ={
            salario_bruto: salario_bruto.value,
            Descontos: Descontos.value,
            Dependentes: Dependentes.value
        }
        console.log("formulario",dados)

        try {
          const  res = await api.post('/salario',dados)
        console.log("apiRes",res)
        setData(res.data)  
        } catch(error){
            console.log(error)
        }   
    }   
        
     return(
        <div>
            <div className="div1">
               <form className="form" onSubmit={submit}>
                <input className="form-item" required name="salario_bruto" type="number" step=".01" placeholder="Salario"  />
                <input className="form-item" required name="Descontos" type="number" step=".01" placeholder="Descontos"/>
                <input className="form-item" required name="Dependentes" type="number" step=".01" placeholder="Dependentes"/>
                <button className="form-button" type="submit">Calcular</button>
            </form> 
            </div>
            <div className="result">
                <ul className="list">
                    <li>Salario Bruto:</li>
                    <li>Desconto INSS:</li>
                    <li>Desconto IRPF:</li>
                    <li>Outros descontos</li>
                    <li>Total descontos:</li>
                    <li>Total a receber:</li>
                </ul>
                <ul className="list">
                    <li>R${data.SalarioBruto ? data.SalarioBruto:'0'}</li>
                    <li>R${data.reajuste_inss ? data.reajuste_inss:'0'}</li>
                    <li>R${data.reajuste_irrf ? data.reajuste_irrf:'0'}</li>
                    <li>R${data.outros_descontos ? data.outros_descontos:'0'}</li>
                    <li>R${data.total_desconto ? data.total_desconto:'0'}</li>
                    <li>R${data.Receber ? data.Receber:'0'}</li>
                </ul>
            </div>
            
        </div>
        

    )   
   
}

export default PostForm