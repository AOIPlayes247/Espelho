# StarControl agente Windows: recebe comandos do site em ws://127.0.0.1:8765
# pip install websockets pydirectinput pynput pyinstaller
# Uso: dê dois cliques em INICIAR-PC.bat (instala as dependências e roda este arquivo)
import asyncio, json, os, sys, ctypes
import websockets, pydirectinput
from pynput.mouse import Controller as Mouse, Button
from pynput.keyboard import Controller as Keyboard

ctypes.windll.user32.SetProcessDPIAware()
W, H = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
pydirectinput.PAUSE = 0
here = os.path.dirname(sys.executable if getattr(sys, "frozen", False) else __file__)
cfg = os.path.join(here, "origin.txt")
if not os.path.exists(cfg):
    open(cfg, "w").write(input("Endereço do seu site (ex: https://usuario.github.io): ").strip().rstrip("/"))
ORIGIN = open(cfg).read().strip()
mouse, kb = Mouse(), Keyboard()
BTN = {"mouseL": Button.left, "mouseR": Button.right}

def valid(k): return k in BTN or k in pydirectinput.KEYBOARD_MAPPING

async def handle(ws):
    async for raw in ws:
        try:
            d = json.loads(raw); t = d["t"]
            if t == "abs": mouse.position = (int(d["x"] * W), int(d["y"] * H))
            elif t == "rel": pydirectinput.moveRel(int(d["dx"]), int(d["dy"]), relative=True)
            elif t == "click":
                if "x" in d: mouse.position = (int(d["x"] * W), int(d["y"] * H))
                mouse.click(BTN["mouseR" if d.get("b") == "right" else "mouseL"], int(d.get("n", 1)))
            elif t == "scroll": mouse.scroll(0, int(d["dy"]))
            elif t in ("down", "up") and valid(d["k"]):
                k = d["k"]
                if k in BTN: (mouse.press if t == "down" else mouse.release)(BTN[k])
                else: (pydirectinput.keyDown if t == "down" else pydirectinput.keyUp)(k)
            elif t == "type": kb.type(str(d["text"])[:200])
            elif t == "combo":
                ks = [str(x) for x in d["keys"][:5] if valid(str(x))]
                for x in ks: pydirectinput.keyDown(x)
                for x in reversed(ks): pydirectinput.keyUp(x)
        except Exception as e:
            print("erro:", e)

async def main():
    async with websockets.serve(handle, "127.0.0.1", 8765, origins=[ORIGIN]):
        print("StarControl ativo e pronto. Origem permitida:", ORIGIN)
        await asyncio.Future()

asyncio.run(main())
