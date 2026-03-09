class ContextoSimples:
    def __enter__(self):
        print("Estou no Enter")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando conexão com segurança!")

with ContextoSimples() as cs:
    print("Execuções em banco de dados!")