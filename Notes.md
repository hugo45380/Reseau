# TP1

## Avantages NAT

Nos machines sont invisibles depuis l'exterieur.

## Inconvénients NAT

Casse l'idée d'avoir une IP par post.



# TP2

## VLAN


Modifie les réseaux sans intervenir physiquement.


### Exo1


Deux réseaux indépendants ne peuvent pas communiquer via un Switch avec le VLAN.




### Exo2

la trame Ethernet est modifier lors de la communication entre 2 switch interconnectés sur un port dot1q.

Ajout d'un Header. Cela permet d'identifier la VLAN visée par le ping du PC Source.


# TP3

## UDP - Sockets

### Exo1

sock.bind(("0.0.0.0", port)) --> publie notre socket sur toutes les interfaces possibles de notre réseau.


data.encode()  -->  converti en octet la chaine de données.


# TP3


### Exo1

socket sans parametres : 

par défault le socket est mis avec SOCK_STREAM =(TCP).



executer le fichier .py sur un terminal et lancer "netcat localhost 5555" sur un autre terminal.


### Exo2