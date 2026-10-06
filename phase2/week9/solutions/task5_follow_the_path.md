# Task 5 — Follow the path out of your house

*(Practices Q3 and Q5. This is a shell task: run each command, paste its real
output, and write a couple of sentences on what it proved.)*

## 1. The routing table — where does everything go?

```
$ netstat -rn -f inet | head
```

**Windows PowerShell:**

```powershell
route print -4
```

```text

**What it showed me:** _which row is the `default` route, what my gateway
address is, and which interface packets leave by._

## 2. The default route in detail

```
$ route -n get default
```

**Windows PowerShell:**

```powershell
Get-NetIPConfiguration; Get-NetIPInterface -AddressFamily IPv4 | Select-Object InterfaceAlias,NlMtu,ConnectionState
```

```text

InterfaceAlias       : Wi-Fi
InterfaceIndex       : 8
InterfaceDescription : Killer(R) Wi-Fi 6E AX1675i 160MHz Wireless Network Adapter (211NGW)
NetProfile.Name      : LIB-Z6W754V
IPv4Address          : 192.168.40.113
IPv6DefaultGateway   :
IPv4DefaultGateway   : 192.168.40.1
DNSServer            : 192.168.40.1


InterfaceAlias  : Conexión de área local* 10
NlMtu           : 1500
ConnectionState : Disconnected


InterfaceAlias  : Conexión de área local* 9
NlMtu           : 1500
ConnectionState : Disconnected


InterfaceAlias  : Wi-Fi
NlMtu           : 1500
ConnectionState : Connected


InterfaceAlias  : Loopback Pseudo-Interface 1
NlMtu           : 4294967295
ConnectionState : Connected

```

**What it showed me:** _the same gateway, plus the interface and the MTU._

## 3. Can I reach my own router?

```
$ ping -c 3 <your-gateway>
```

**Windows PowerShell:**

```powershell
ping -n 3 -w 1000 192.168.40.1
```

```text

Haciendo ping a 192.168.40.1 con 32 bytes de datos:
Respuesta desde 192.168.40.1: bytes=32 tiempo=3ms TTL=64
Respuesta desde 192.168.40.1: bytes=32 tiempo=3ms TTL=64
Respuesta desde 192.168.40.1: bytes=32 tiempo=2ms TTL=64

Estad�sticas de ping para 192.168.40.1:
    Paquetes: enviados = 3, recibidos = 3, perdidos = 0
    (0% perdidos),
Tiempos aproximados de ida y vuelta en milisegundos:
    M�nimo = 2ms, M�ximo = 3ms, Media = 2ms
```

**What it showed me:** _the round trip to the first hop — the floor under
every other measurement. If it times out, see the note below._

## 4. The whole path to a distant host

```
$ traceroute -n -q 1 -w 1 example.com
```

**Windows PowerShell:**

```powershell
tracert -d -h 12 -w 500 example.com
```

```text

Traza a la direcci�n example.com [172.66.147.243]
sobre un m�ximo de 12 saltos:

  1     2 ms     3 ms     2 ms  192.168.40.1
  2    11 ms    10 ms     8 ms  100.96.0.3
  3    14 ms     8 ms     7 ms  186.15.129.29
  4     *        *        *     Tiempo de espera agotado para esta solicitud.
  5    11 ms     8 ms     7 ms  186.159.248.201
  6     8 ms     9 ms     9 ms  172.16.1.205
  7     8 ms     8 ms     9 ms  186.15.241.103
  8     8 ms    33 ms     9 ms  172.66.147.243

Traza completa.
```

**What it showed me:** _which hop is my own router, where the latency jumps
(that's usually the leap out of my ISP), and where stars appear._

## Two surprises to account for

1. **A gateway that ignores `ping` but answers traceroute's hop 1.** Filtered
   ICMP is not a down host — and mistaking one for the other is a classic
   false alarm. Note whether this happened to you and how you know the
   gateway is fine anyway.
2. **Hops with `10.x` addresses.** Q4's private ranges are in use inside your
   ISP's own network too, so a private address in the middle of a traceroute
   is normal, not a misconfiguration.
