#!/bin/bash
SEARCH="firefox"
ALVO="$1"
echo "Exemplo de utilização do google dork"
$SEARCH "https://google.com/search?q=site:pastebinx.com+$ALVO"
