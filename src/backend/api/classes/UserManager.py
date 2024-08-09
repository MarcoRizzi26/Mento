import pydantic
from typing import List, Optional
from fastapi.responses import JSONResponse

class User(pydantic.BaseModel):
    nome: str
    email: str
    idade: Optional[int] = None

    def toDict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "idade": self.idade
        }

class UserManager:
    users: List[User] = []

    def insert(self, user: User):
        try:
            if any(u.email == user.email for u in self.users):
                return JSONResponse(content={
                    "error": True,
                    "message": "Usuário já cadastrado"
                }, status_code=409)

            self.users.append(user)
        except Exception as error:
            return JSONResponse(content={
                "error": True,
                "message": f"Erro ao cadastrar o usuário: {error}"
            }, status_code=500)

        return JSONResponse(content={
            "error": False,
            "message": "Usuário cadastrado com sucesso"
        }, status_code=201)

    def update(self, email: str, user: User):
        try:
            for u in self.users:
                if u.email == email:
                    u.nome = user.nome
                    u.idade = user.idade
                    return JSONResponse(content={
                        "error": False,
                        "message": "Usuário atualizado com sucesso"
                    }, status_code=200)

            return JSONResponse(content={
                "error": True,
                "message": "Usuário não encontrado"
            }, status_code=404)
        except Exception as error:
            return JSONResponse(content={
                "error": True,
                "message": f"Erro ao atualizar o usuário: {error}"
            }, status_code=500)

    @classmethod
    def delete(cls, email: str):
        try:
            for u in cls.users:
                if u.email == email:
                    cls.users.remove(u)
                    return JSONResponse(content={
                        "error": False,
                        "message": "Usuário deletado com sucesso"
                    }, status_code=200)

            return JSONResponse(content={
                "error": True,
                "message": "Usuário não encontrado"
            }, status_code=404)
        except Exception as error:
            return JSONResponse(content={
                "error": True,
                "message": f"Erro ao deletar o usuário: {error}"
            }, status_code=500)

    @classmethod
    def select(cls, email: str):
        try:
            for u in cls.users:
                if u.email == email:
                    return JSONResponse(content={
                        "error": False,
                        "message": "Usuário carregado com sucesso",
                        "user": u.toDict()
                    }, status_code=200)

            return JSONResponse(content={
                "error": True,
                "message": "Usuário não encontrado"
            }, status_code=404)
        except Exception as error:
            return JSONResponse(content={
                "error": True,
                "message": f"Erro ao carregar o usuário: {error}"
            }, status_code=500)

    @classmethod
    def select_all(cls):
        try:
            users = [user.toDict() for user in cls.users]
            return JSONResponse(content={
                "error": False,
                "message": "Usuários carregados com sucesso",
                "users": users
            }, status_code=200)
        except Exception as error:
            return JSONResponse(content={
                "error": True,
                "message": f"Erro ao carregar os usuários: {error}"
            }, status_code=500)