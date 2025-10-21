#/bin/bash

echo ""
ip_publica=$(curl ifconfig.me)
echo ""
echo "La dirección IP pública es: $ip_publica"

echo ""
ip_privada=$(hostname -I | awk '{print $1}')
echo "La dirección IP privada es: $ip_privada"
