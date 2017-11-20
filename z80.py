import desensamblador

class Z80(object):
    # Registros son declarados como cadenas en hexadecimal
    B = "00"
    C = "00"
    D = "00"
    E = "00"
    H = "00"
    L = "00"
    A = "00"
    F = "00"
    SP = "65034"
    IX = "00"
    IY = "00"
    PC = "00"
    IFF1 = "00"
    IFF2 = "00"
    I = "00"
    R = "00"

    @staticmethod
    def hexToBin(numHex):
        return bin(int(numHex, 16))[2:].zfill(8)
    @staticmethod
    def binToHex(numBin):
        return hex(int(numBin, 2))[2:].zfill(2)

    # El 7 es porque el bit 0 se encuentra en el lado derecho, mientras que la posición 0
    # en un arreglo esta a la izquierda
    @staticmethod
    def changeFlag(bitIndex, val):
        Z80.F = Z80.hexToBin(Z80.F)
        Z80.F = Z80.F[:7 - bitIndex] + val + Z80.F[7 - bitIndex + 1:]
        Z80.F = Z80.binToHex(Z80.F)
        return Z80.F