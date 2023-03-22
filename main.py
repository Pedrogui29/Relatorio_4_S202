from save_json import writeAJson
from database import Database
from ProductAnalyzer import gasto_cliente_B
from ProductAnalyzer import produto_menos_vendido
from ProductAnalyzer import cliente_que_menos_gastou_em_uma_unica_compra
from ProductAnalyzer import produtos_vendidos_acima_de_2_unidades

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()
data = db.collection.find()

# Escrevendo json do gasto do cliente B
result = gasto_cliente_B()
writeAJson(result, "gasto_cliente_B")

#Escrevendo Json do produto maais vendido
result2 = produto_menos_vendido()
writeAJson(result2, "produto_menos_vendido")

#Escrevendo Json do cliente que menos gastou
result3 = cliente_que_menos_gastou_em_uma_unica_compra()
writeAJson(result3, "cliente_que_menos_gastou_em_uma_unica_compra")

#Escrevendo Json dos produtos vendidos acima de 2 unidades
result4 = produtos_vendidos_acima_de_2_unidades()
writeAJson(result4, "produtos_vendidos_acima_de_2_unidades")