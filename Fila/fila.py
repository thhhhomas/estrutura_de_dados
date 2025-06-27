from typing import Optional

class Item(object):
    def __init__(self, conteudo: Optional[int] = None):
        self.conteudo = conteudo
        self.prox: Optional["Item"] = None

class Fila(object):
    def __init__(self):
        self.inicio = Item()
    
    def enqueue(self, conteudo: int) -> None:
        item = self.inicio
        while(True):
            if self.empty():
                self.inicio.conteudo = conteudo
                break
            if not item.prox:
                item.prox = Item(conteudo=conteudo)
                break
            item = item.prox
    
    def tam(self) -> int:
        if self.empty():
            return 0
        cont = 1
        item = self.inicio
        while(True):
            if item.prox:
                cont+=1
                item = item.prox
            else:
                return cont

    def empty(self) -> bool:
        return self.inicio.conteudo is None

    def print_fila(self) -> None:
        if self.empty():
            print("Lista vazia")
            return
        item = self.inicio
        retorno = "["
        while(True):
            if not item:
                retorno += " ]"
                break
            retorno += f" <{item.conteudo}>"
            item = item.prox
        print(retorno)
            
    def dequeue(self) -> Optional[int]:
        if self.empty():
            print("Fila vazia")
            return None
        conteudo = self.inicio.conteudo
        self.inicio = self.inicio.prox
        return conteudo

def main():
    fila = Fila()
    
    print(f"Fila vazia: {fila.empty()}")

    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)

    print(f"Fila vazia: {fila.empty()}")

    print(f"Fila:")
    fila.print_fila()

    fila.enqueue(fila.dequeue())

    print(f"Fila:")
    fila.print_fila()

    print(f"Tamanho da fila: {fila.tam()}")

    print(f"Item removido: {fila.dequeue()}")

    print(f"Tamanho da fila: {fila.tam()}")

    print(f"Fila:")
    fila.print_fila()

if __name__ == "__main__":
    main()
