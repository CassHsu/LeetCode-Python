class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        tmp = ''
        
        while dominoes != tmp:
            tmp = dominoes
            dominoes = dominoes.replace('R.L', 'XXX')
            dominoes = dominoes.replace('R.', 'RR')
            dominoes = dominoes.replace('.L', 'LL')

        return  dominoes.replace('XXX', 'R.L')
