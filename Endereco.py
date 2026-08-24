class Endereco:
    def __init__(self, rua, numero, bairro, cidade, estado, cep):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    def atualizarEndereco(self, rua, numero, bairro, cidade, estado, cep):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep
    def validarEndereco(self):
        return (
            self.__rua != "" and 
            self.__numero != "" and
            self.__bairro != "" and
            self.__cidade != "" and
            self.__estado != "" and
            self.__cep != ""
            )
             
