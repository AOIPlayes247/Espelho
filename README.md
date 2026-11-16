# StarControl

Controle o Windows pelo celular (WebRTC + PeerJS), 100% pela web.

## Publicar no GitHub Pages
1. Crie um repositório e envie TODOS os arquivos desta pasta para a raiz (index.html, manifest.json, sw.js, icon-192.png, icon-512.png, icon.svg).
2. Settings -> Pages -> Source: Deploy from a branch -> Branch: main, pasta / (root) -> Save.
3. Abra https://SEU-USUARIO.github.io/NOME-DO-REPO/ (leva cerca de 1 minuto).

## Usar
- PC: no site, clique em "Baixar Launcher para PC" (gera agent.py + INICIAR-PC.bat). Deixe na mesma pasta, instale o Python (marque "Add Python to PATH") e dê dois cliques no INICIAR-PC.bat. O painel abre em http://localhost:8766.
- No painel do PC: anote o código e clique em "Iniciar Transmissão de Tela".
- Celular: abra o site (ou escaneie o QR), conecte com o código, toque em "Instalar Web App no Celular" se quiser o atalho. No PC, clique OK em "Permitir que um dispositivo controle este PC?".

A pasta src-pc/ é só referência do código do agente (não precisa ir ao repositório).
