class Retangulo():
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None
        self.base = base
        self.altura = altura
        

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, b):
        if not isinstance(b, float) and not isinstance(b, int):
            raise TypeError('O valor da base deve ser um número')
        if b <= 0:
            raise ValueError('Valor inválido para base')
        else:
            self._base = b


    @property
    def altura(self):
        return self._altura
   
    @altura.setter
    def altura(self, h):
        if not isinstance(h, float) and not isinstance(h, int):
            raise TypeError('O valor da altura deve ser um número.')
        if h <= 0:
            raise ValueError('Valor inválido para altura')
        else:
            self._altura = h


    @property
    def medidas(self):
        return f'''Base = {self.base}
Altura = {self.altura}
Área = {self.area}'''
    
    @medidas.setter
    def medidas(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError('As medidas devem ser informadas dentro de uma tupla')
        if len(valores) != 2:
            raise ValueError('Informe uma tupla com apenas dois valores numéricos')
        
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError('A base deve ser um número')
        
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError('A altura deve ser um número')
    
    
    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area
    
    @area.setter
    def area(self):
        raise PermissionError('Área não pode ser configurada desse jeito.')

   