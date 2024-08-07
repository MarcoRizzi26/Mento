from fastapi import APIRouter

from modules.api.classes.Kit import Kit

router = APIRouter()

@router.get('/{Nome}')
async def read_one(Nome: str):
	return Kit.select(Nome)

@router.get('/')
async def read_all():
	return Kit.select_all()


@router.get('/joined/{Nome}')
async def read_joined(Nome: str):
	return Kit.select_joined(Nome)


@router.post('/')
async def create(kit: Kit):
	return kit.insert()


@router.put('/{Nome}')
async def update(Nome: str, kit: Kit):
	return kit.update(Nome)


@router.delete('/{Nome}')
async def delete(Nome: str):
	return Kit.delete(Nome)


#? Nao sei da onde veio esse código mas ta errado - Gustavo
# @router.delete('/tela-inicial')
# async def chamada_tela_inicial():
# 	return Kit.chamada_tela_inicial()