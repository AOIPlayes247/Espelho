# StarControl

Controle o Windows pelo celular (WebRTC + PeerJS), 100% pela web.

## Estrutura do repositório
```
index.html        site completo (HTML, CSS e JS)
manifest.json     Web App (instalar no celular)
sw.js             service worker (cache)
assets/           logo, favicon e ícones do app
```

## Publicar no GitHub Pages
1. Envie TODOS os arquivos e a pasta `assets/` para a raiz do repositório (mantenha a pasta assets).
2. Settings -> Pages -> Source: Deploy from a branch -> Branch: main, pasta / (root) -> Save.
3. Abra https://SEU-USUARIO.github.io/NOME-DO-REPO/ (leva cerca de 1 minuto).

## Usar
- PC: no site, clique em "Baixar Launcher para PC" (gera agent.py + INICIAR-PC.bat). Deixe na mesma pasta, instale o Python (marque "Add Python to PATH") e dê dois cliques no INICIAR-PC.bat. O painel abre em http://localhost:8766.
- No painel do PC: escolha a qualidade, anote o código e clique em "Iniciar Transmissão de Tela".
- Celular: abra o site (ou escaneie o QR), conecte com o código e toque em "Instalar Web App no Celular" se quiser o atalho. No PC, clique OK em "Permitir que um dispositivo controle este PC?".
