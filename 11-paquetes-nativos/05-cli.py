import os
import sys
from pathlib import Path


def cli(args):
    if len(args) == 1:
        print("No se pasaron args")
        return
    if len(args) != 3:
        print("No se pasaron args validos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("origen no existe")
        return
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino ya existe")
        return

    os.rename(str(origen), str(destino))
    print("Archivo renombrado con exito!")


cli(sys.argv)
