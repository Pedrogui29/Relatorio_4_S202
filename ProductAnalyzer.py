from database import Database

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()
data = db.collection.find()

#1 Retorne o total de gastos do cliente B
def gasto_cliente_B():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$match": {"cliente_id":"B"}},
        {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    ])

#2 Retorne o produto menos vendido de todas as compras
def produto_menos_vendido():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": 1}},
        {"$limit": 1}
    ])


#3 Busque o cliente que menos gastou em uma única compra
def cliente_que_menos_gastou_em_uma_unica_compra():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"_id.data": 1, "total": 1}},
        {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
    ])


#4 Mostre todos os produtos que foram vendidos acima de 2 unidades
def produtos_vendidos_acima_de_2_unidades():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
        {"$match": {"quantidade": {"$gt":2}}}
    ])