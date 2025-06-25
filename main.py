# Função criada para salvar o conteúdo de texto em um arquivo no caminho especificado
def salvar_texto(texto, path):
    with open(path, 'w') as arquivo:
        arquivo.write(texto)
    print(f'Arquivo salvo como {path}')

# Classe responsável por realizar a fatoração LU de uma matriz A e resolver o sistema AX = B
class FatoracaLU:
    def __init__(self, A, B):
        self.A = A  # Matriz dos coeficientes
        self.B = B  # Matriz dos termos independentes
        self.lines = len(A)  # Número de linhas da matriz A
        self.coluns = len(A[0])  # Número de colunas da matriz A
        self.U = [row[:] for row in A]  # Inicializa U como uma cópia de A (para manter A intacta)

        # Inicializa L como uma matriz identidade modificada (1s na diagonal e 0 acima da diagonal)
        self.L = [[1 if colun == line else 0 if colun > line else None
                   for colun in range(self.coluns)] for line in range(self.lines)]

    # Função geradora que define a ordem dos pivôs para a eliminação de Gauss
    def Pivos(self):
        diagonalColun = 0
        for colun in range(self.coluns):
            for line in range(self.lines - 1, diagonalColun, -1):
                yield (line, colun)
            diagonalColun += 1

    # Executa os passos da fatoração LU e armazena as transformações feitas
    def passos(self):
        transformations = []  # Armazena o histórico das transformações

        for orden, (line, colun) in enumerate(self.Pivos()):
            # Evita divisão por zero ao identificar pivô nulo
            if self.U[colun][colun] == 0:
                continue

            # Calcula o multiplicador (pivô)
            pivo = self.U[line][colun] / self.U[colun][colun]
            self.L[line][colun] = pivo  # Armazena o valor do pivô na matriz L

            # Atualiza a linha atual da matriz U (eliminação gaussiana)
            for colune, valor in enumerate(self.U[line][:]):
                self.U[line][colune] = valor - pivo * self.U[colun][colune]

            # Salva o estado atual da matriz U e o pivô usado
            transformations.append({
                'orden': orden,
                'table': [row[:] for row in self.U],
                'pivo': {
                    'pivo': pivo,
                    'local': (line, colun)
                }
            })

        # Retorna os resultados finais
        return {
            'transformations': transformations,
            'L': self.L,
            'U': self.U
        }

# Função para capturar os valores de uma matriz digitada pelo usuário
def getMatriz(m, tamanho):
    linhas, colunas = tamanho
    print(f'Construindo a matriz {m}')
    matriz = [[(linha, coluna) for coluna in range(colunas)] for linha in range(linhas)]

    # Solicita os elementos da matriz via input
    for linha in range(linhas):
        for coluna in range(colunas):
            matriz[linha][coluna] = float(input(f'Informe o elemento da linha {linha+1} e coluna {coluna+1}: '))
    return matriz

# Converte a matriz em uma string legível para saída no arquivo (em forma de tabela formatada)
def porExtenso(matriz):
    pex = ''
    for n, linha in enumerate(matriz):
        elementos = '\t'.join([
            f'\t {elemento:.2f}' if elemento % 1 != 0 else f'\t {elemento:.0f}'
            for elemento in linha
        ])
        elementos = elementos.replace(' -', '-')  # Ajusta espaçamentos com sinais
        elementos = elementos.replace('-0', ' 0')  # Evita aparecer -0
        pex += f'Linha {n+1}:{elementos}\n'
    return pex

# Resolve o sistema LUX = B em duas etapas: LY = B (progressiva), UX = Y (regressiva)
def getXY(A, B, L, U):
    # Extrai a coluna B como vetor simples
    B = [linha[0] for linha in B]

    # Substituição progressiva para resolver LY = B
    def substituicao_progressiva(L, B):
        n = len(B)
        Y = [0] * n
        for i in range(n):
            soma = sum(L[i][j] * Y[j] for j in range(i))
            Y[i] = (B[i] - soma) / L[i][i]
        return Y

    # Substituição regressiva para resolver UX = Y
    def substituicao_regressiva(U, Y):
        n = len(Y)
        X = [0] * n
        for i in reversed(range(n)):
            soma = sum(U[i][j] * X[j] for j in range(i + 1, n))
            try:
                X[i] = (Y[i] - soma) / U[i][i]
            except:
                X[i] = float('nan')  # Evita crash se U[i][i] for zero
        return X

    Y = substituicao_progressiva(L, B)
    X = substituicao_regressiva(U, Y)

    # Retorna os resultados em forma de matriz coluna (para porExtenso funcionar igual)
    return ([[x] for x in X], [[y] for y in Y])

# Execução principal do programa
if __name__ == '__main__':
    # Solicita o nome do arquivo de saída
    nomeArquivo = input('Informe o nome a ser salvo: exemplo "nomearquivo.txt": ')
    
    # Solicita o tamanho da matriz A (quadrada)
    tamanho = int(input('Qual o tamanho da matriz quadrada A?: '))
    
    # Captura a matriz A do usuário
    A = getMatriz('A', (tamanho, tamanho))

    # Captura a matriz B do usuário
    B = getMatriz('B', (tamanho, 1))

    # Cria a instância da fatoração LU
    nova_fatoracao = FatoracaLU(A, B)

    # Executa a fatoração
    P = nova_fatoracao.passos()
    L = P['L']
    U = P['U']

    # Resolve o sistema para encontrar X e Y
    X, Y = getXY(A, B, L, U)

    # Cria a mensagem final com todos os dados formatados
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

    # Salva o relatório gerado no arquivo especificado
    salvar_texto(mensagen_de_retorno, nomeArquivo)
