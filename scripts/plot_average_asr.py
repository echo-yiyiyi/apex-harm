"""Render the paper's reported Average ASR values in the reference figure's style."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ROWS = [
    ('Claude Opus 5', 8, 'anthropic'), ('Claude Sonnet 5', 20, 'anthropic'),
    ('GPT-6 Astra', 28, 'openai'), ('Gemini 3.8 Flash', 33, 'google'),
    ('GPT-5.6 Luna', 42, 'openai'), ('Gemini 3.7 Flash', 46, 'google'),
    ('Kimi K3', 47, 'kimi'), ('DeepSeek V4 Flash', 47, 'deepseek'),
    ('GPT-5.6 Sol', 52, 'openai'), ('GLM 5.3 Flash', 57, 'glm'),
    ('GPT-5.6 Terra', 57, 'openai'), ('Gemini 3.6 Flash', 58, 'google'),
]
PALETTE = {
    'anthropic': ('#d67c59', '#ffd0a9'), 'openai': ('#f9df35', '#b5d3f1'),
    'google': ('#4285ed', '#d96374'), 'kimi': ('#edf47a', '#b5b93e'),
    'deepseek': ('#5374dd', '#9cd9f2'), 'glm': ('#7971bd', '#cbbce6'),
}
S = 2
im = Image.new('RGB', (1120*S, 1570*S), 'white')
d = ImageDraw.Draw(im)
font_root = Path('/System/Library/Fonts/Supplemental')
def font(size, bold=False):
    candidates = [font_root / ('Arial Bold.ttf' if bold else 'Arial.ttf'),
                  Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
    return ImageFont.truetype(str(next(p for p in candidates if p.exists())), size*S)
def text(x, y, value, size, fill='#15171b', bold=False, anchor=None):
    d.text((x*S,y*S), value, font=font(size,bold), fill=fill, anchor=anchor)
def rgb(h):
    return tuple(int(h[i:i+2],16) for i in (1,3,5))
text(48,32,'APEX-Harm',48,bold=True)
text(48,95,'Average attack success rate (ASR)',28)
text(48,137,'Categories 1–6 · Lower is better',22,fill='#626b78')
left, right, width = 48, 1072, 1024
for i,(name,value,family) in enumerate(ROWS):
    y = 205+i*104
    text(left,y,name,30)
    text(right,y,f'{value}%',30,fill='#374151',anchor='ra')
    by, bh = (y+45)*S, 26*S
    d.rounded_rectangle((left*S,by,right*S,by+bh),radius=13*S,fill='#f1f3f5')
    w = round(width*value/60*S)
    grad = Image.new('RGB',(w,bh))
    gd = ImageDraw.Draw(grad)
    a,b = map(rgb,PALETTE[family])
    for x in range(w):
        t=x/max(1,w-1)
        gd.line((x,0,x,bh),fill=tuple(round(u+(v-u)*t) for u,v in zip(a,b)))
    mask=Image.new('L',(width*S,bh),0)
    ImageDraw.Draw(mask).rounded_rectangle((0,0,width*S,bh),radius=13*S,fill=255)
    im.paste(grad,(left*S,by),mask.crop((0,0,w,bh)))
axis=1473
d.line((left*S,axis*S,right*S,axis*S),fill='#dce0e5',width=2*S)
for tick in (0,20,40,60):
    x=left+width*tick/60
    text(x,axis+18,f'{tick}%',22,fill='#828b98',anchor='ma')
text(left,1532,'Reported paper averages; confidence intervals were not provided.',17,fill='#626b78')
im.save(ROOT / 'assets' / 'average-asr.png')
