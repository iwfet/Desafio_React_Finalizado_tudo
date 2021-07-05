from flask import *
from API import app, db
from .models import INSS, IRFF
import json

@app.route('/',methods=['GET'])
def home():
    return {"dado":"ola mundo"}

@app.route('/salario', methods=['POST'])
def salario():
    if(request.method =='POST'):
        
        Salario_bruto = float(request.json["salario_bruto"])
        Descontos =  float(request.json["Descontos"])
        Dependentes = int(request.json["Dependentes"])
        
        
        inss = INSS.query.filter(INSS.faixa_inicial <= Salario_bruto) or (INSS.faixa_final >= Salario_bruto)   
        for ins in inss:
            aliquota = (ins.aliquota/100)
            deducao = ins.deduçao
          
        reajuste_inss = (Salario_bruto*aliquota)-float(deducao)  
        
        if (Salario_bruto >= 1903.98):  
            salariobase = Salario_bruto - (Descontos + (189.59 * Dependentes ))
            print(salariobase)
            irrf = IRFF.query.filter(IRFF.faixa_inicial <= float(salariobase)) or (IRFF.faixa_final >= float(salariobase))
            for inf in irrf:
                aliquotairrf = (inf.aliquota/100)
                deducaoirrf = inf.deduçao            
            reajuste_irrf = (salariobase*aliquotairrf) - float(deducaoirrf)
        else:
            reajuste_irrf = 0   

        valor_inss = round(abs(reajuste_inss),2)
        valor_irrf = round(abs(reajuste_irrf),2)
        Desconto = round(abs(reajuste_inss + reajuste_irrf),2)
        Receber = Salario_bruto - Desconto 
    
    return {
        "SalarioBruto": Salario_bruto,
        "reajuste_inss":valor_inss,
        "reajuste_irrf":valor_irrf,
        "outros_descontos":Descontos,
        "total_desconto":Desconto,
        "Receber":Receber
          }
    
    