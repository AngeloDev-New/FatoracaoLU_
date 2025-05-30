
# funcao criada para salvamento da saida, ela contem duas entradas 'texto':sera o conteudo do arquivo gerado e 'path':que infora o local que o mesmo e gerado
def salvar_texto(texto,path):
    with open(path,'w') as arquivo:
        arquivo.write(texto)
    print(f'Arquivo salvo como {path}')
#Classe criada para fatorar a matriz A em L,U trazendo o passo a passo para obter X e Y a partir de B
class FatoracaLU:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.lines = len(A)
        self.coluns = len(A[0])
        self.U = [row[:] for row in A]  # cópia profunda
        # Inicializa L com 1 na diagonal e 0 acima da diagonal
        self.L = [[1 if colun == line else 0 if colun > line else None
                   for colun in range(self.coluns)] for line in range(self.lines)]

    def Pivos(self):
        diagonalColun = 0
        for colun in range(self.coluns):
            for line in range(self.lines - 1, diagonalColun, -1):
                yield (line, colun)
            diagonalColun += 1

    def passos(self):
        transformations = []
        for orden, (line, colun) in enumerate(self.Pivos()):
            # Evita divisão por zero (pivo zero)
            if self.U[colun][colun] == 0:
                continue

            pivo = self.U[line][colun] / self.U[colun][colun]
            self.L[line][colun] = pivo

            for colune, valor in enumerate(self.U[line][:]):
                self.U[line][colune] = valor - pivo * self.U[colun][colune]
            
            transformations.append({
                'orden': orden,
                'table': [row[:] for row in self.U],
                'pivo':{
                    'pivo':pivo,
                    'local':(line,colun)
                }

            })

        return {
            'transformations': transformations,
            'L': self.L,
            'U': self.U
        }

def getMatriz(m,tamanho):
    linhas,colunas = tamanho
    print(f'Construindo a matriz {m}')
    matriz = [[(linha,coluna) for coluna in range(colunas)] for linha in range(linhas)]
    for linha in range(linhas):
        for coluna in range(colunas):
            matriz[linha][coluna] = float(input(f'Informe o elemento da linha {linha+1} e coluna {coluna+1}: '))
    return matriz
# aqui esta funcao recebe  matriz e a descreve pra jogar no arquivo de saida
def porExtenso(matriz):
    pex = ''
    for n, linha in enumerate(matriz):
        elementos = '\t'.join([
            f'\t {elemento:.2f}' if elemento % 1 != 0 else f'\t {elemento:.0f}'
            for elemento in linha
        ])
        elementos = elementos.replace(' -', '-')
        elementos = elementos.replace('-0', ' 0')
        pex += f'Linha {n+1}:{elementos}\n'
    return pex
# def getXY(A,B,L,U):
#     # AX = B
#     # LUX = B
#     # UX = Y SEGUNDO CRITERIO
#     # LY = B PRIMEIRO CRITERIO
#     return (X,Y)
def getXY(A, B, L, U):
    B = [linha[0] for linha in B]
    def substituicao_progressiva(L, B):
        n = len(B)
        Y = [0] * n
        for i in range(n):
            soma = sum(L[i][j] * Y[j] for j in range(i))
            Y[i] = (B[i] - soma) / L[i][i]
        return Y

    def substituicao_regressiva(U, Y):
        n = len(Y)
        X = [0] * n
        for i in reversed(range(n)):
            soma = sum(U[i][j] * X[j] for j in range(i+1, n))
            X[i] = (Y[i] - soma) / U[i][i]
        return X

    Y = substituicao_progressiva(L, B)
    X = substituicao_regressiva(U, Y)
    return ([[x] for x in X], [[y] for y in Y])

if __name__ == '__main__':
    nomeArquivo = input('Informe o nome a ser salvo: exemplo "nomearquivo.txt": ')
    tamanho = int(input('Qual o tamanho da matriz quadrada A?: '))
    A = getMatriz('A',(tamanho,tamanho))
    # print(*A)
    B = getMatriz('B',(tamanho,1))
    nova_fatoracao = FatoracaLU(A,B)
    # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>',nova_fatoracao.passos(),'<<<<<<<<<<<<<<<<<<<<<<<<<')
    P = nova_fatoracao.passos()
    L = P['L']
    U = P['U']
    # print("DEBUG L:", L)
    # print(porExtenso(L))

    X,Y=getXY(A,B,L,U)
    
    mensagen_de_retorno = f'''
Foi inicialmente entregue uma matriz A de ordem {tamanho}
sendo ela: 
{porExtenso(A)} 
e a matriz B:
{porExtenso(B)}
Tendo como saida a matriz L
{porExtenso(L)}
E a matriz U
{porExtenso(U)}
Resultando no Y:
{porExtenso(Y)}
e finalmente X:
{porExtenso(X)}

'''
    salvar_texto(mensagen_de_retorno,nomeArquivo)

exemplo_saida_passos =  {
    'transformations': [
        {
            'orden': 0,
            'table': [
                [1.0, 2.0, 4.0],
                [5.0, 1.0, 2.0],
                [0.0, -10.0, -19.0]
                ],
            'pivo': {
                'pivo': 6.0,
                'local': (2, 0)
                }
        },
        {
            'orden': 1,
            'table': [
                [1.0, 2.0, 4.0],
                [0.0, -9.0, -18.0],
                [0.0, -10.0, -19.0]
                ], 
            'pivo': {
                'pivo': 5.0,
                'local': (1, 0)
                }
        }, 
        {
            'orden': 2, 
            'table': [
                [1.0, 2.0, 4.0], 
                [0.0, -9.0, -18.0], 
                [0.0, 0.0, 1.0]], 
            'pivo': {
                'pivo': 1.1111111111111112, 
                'local': (2, 1)
                }
        }
        ], 
    'L': [
        [1, 0, 0], 
        [5.0, 1, 0], 
        [6.0, 1.1111111111111112, 1]
        ], 
    'U': [
        [1.0, 2.0, 4.0], 
        [0.0, -9.0, -18.0], 
        [0.0, 0.0, 1.0]
        ]
}