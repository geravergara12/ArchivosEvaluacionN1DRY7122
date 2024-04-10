def determinar_tipo_acl(numero_acl):

    if numero_acl.isdigit():
        numero_acl = int(numero_acl)
        if 1 <= numero_acl <= 99:
            return "ACL Estándar"
        elif 100 <= numero_acl <= 199:
            return "ACL Extendida"
        else:
            return "El número no corresponde a una lista de acceso."
    else:
        return "El número de ACL no es válido."

def main():
    numero_acl = input("Ingrese el número de ACL IPv4: ")

    tipo_acl = determinar_tipo_acl(numero_acl)
    print("Tipo de ACL:", tipo_acl)

if __name__ == "__main__":
    main()
