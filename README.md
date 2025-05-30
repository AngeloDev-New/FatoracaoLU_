# Projeto de Acessibilidade: Fatoração LU

Este projeto foi desenvolvido com foco em **acessibilidade** e tem como objetivo resolver **sistemas lineares** de ordem `n x n` (matrizes quadradas) por meio da **fatoração LU**, **sem o uso de bibliotecas externas**.

---

## 📌 Objetivos

- Oferecer uma ferramenta acessível para estudantes e professores.
- Permitir a resolução de sistemas lineares utilizando decomposição LU.
- Garantir que leitores de tela possam interpretar facilmente a interface.

---

## 🚀 Como executar

1. Certifique-se de que você possui o Python 3 instalado.
2. Rode o programa principal com:

```bash
python main.py
```

Ou utilize um arquivo de entrada com redirecionamento:

```bash
python main.py < entrada_exemplo.txt
```

---

## 📁 Arquivos principais

- `main.py`: Script principal que conduz toda a lógica do programa.
- `entrada_exemplo.txt` (opcional): Arquivo de exemplo para entrada automatizada de dados.
- `README.md`: Este arquivo, com as instruções.

---

## ✅ Requisitos

- Python 3.x
- Nenhuma biblioteca adicional é necessária.

---

## ♿ Acessibilidade

- Todas as mensagens foram pensadas para funcionar com **leitores de tela**.
- O texto é claro, direto e compatível com ferramentas como o **Orca (Linux)**.

---

## ✍️ Exemplo de entrada

```
Informe o nome a ser salvo: exemplo "nomearquivo.txt": saida_exemplo.txt
Qual o tamanho da matriz quadrada A?: 3       
Construindo a matriz A
Informe o elemento da linha 1 e coluna 1: 1
Informe o elemento da linha 1 e coluna 2: 2
Informe o elemento da linha 1 e coluna 3: 4
Informe o elemento da linha 2 e coluna 1: 5
Informe o elemento da linha 2 e coluna 2: 1
Informe o elemento da linha 2 e coluna 3: 2
Informe o elemento da linha 3 e coluna 1: 6
Informe o elemento da linha 3 e coluna 2: 2
Informe o elemento da linha 3 e coluna 3: 4
Construindo a matriz B
Informe o elemento da linha 1 e coluna 1: 5
Informe o elemento da linha 2 e coluna 1: 4
Informe o elemento da linha 3 e coluna 1: 5
```

---

## 📤 Saída esperada

```
Foi inicialmente entregue uma matriz A de ordem 3
sendo ela: 
Linha 1:	 1		 2		 4
Linha 2:	 5		 1		 2
Linha 3:	 6		 2		 5
 
e a matriz B:
Linha 1:	 5
Linha 2:	 4
Linha 3:	 5

Tendo como saida a matriz L
Linha 1:	 1		 0		 0
Linha 2:	 5		 1		 0
Linha 3:	 6		 1.11		 1

E a matriz U
Linha 1:	 1		 2		 4
Linha 2:	 0		-9		-18
Linha 3:	 0		 0		 1

Resultando no Y:
Linha 1:	 5
Linha 2:	-21
Linha 3:	-1.67

e finalmente X:
Linha 1:	 0.33
Linha 2:	 5.67
Linha 3:	-1.67
```

---

## 🧠 Créditos

Desenvolvido por AngeloDev-New, com foco em educação, acessibilidade e matemática aplicada.
