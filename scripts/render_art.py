from pathlib import Path
import html
import math

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(exist_ok=True)

def save(name, w, h, title, body, defs=''):
    (OUT/name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}"><title>{html.escape(title)}</title><defs>{defs}</defs>{body}</svg>''', encoding='utf-8')

defs = '''<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#080d1d"/><stop offset=".65" stop-color="#141d38"/><stop offset="1" stop-color="#27163f"/></linearGradient>
<linearGradient id="accent"><stop stop-color="#67e8f9"/><stop offset=".55" stop-color="#818cf8"/><stop offset="1" stop-color="#e879f9"/></linearGradient>
<radialGradient id="halo"><stop stop-color="#7c3aed" stop-opacity=".35"/><stop offset="1" stop-color="#7c3aed" stop-opacity="0"/></radialGradient>
<linearGradient id="top" x2="1" y2="1"><stop stop-color="#a5f3fc"/><stop offset="1" stop-color="#818cf8"/></linearGradient>
<linearGradient id="left" x2="1" y2="1"><stop stop-color="#2563eb"/><stop offset="1" stop-color="#16336a"/></linearGradient>
<linearGradient id="right" x2="1" y2="1"><stop stop-color="#c084fc"/><stop offset="1" stop-color="#6d28d9"/></linearGradient>'''

body = '<rect width="1200" height="380" rx="26" fill="url(#bg)"/><rect x="1" y="1" width="1198" height="378" rx="25" fill="none" stroke="#334065"/>'
body += '<circle cx="970" cy="190" r="210" fill="url(#halo)"/>'
for i in range(13):
    x=700+i*45
    body += f'<path d="M{x} 275l-175 105 M{x} 275l175 105" stroke="#5e6ba5" stroke-opacity=".11"/>'
for i in range(5):
    body += f'<path d="M680 {280+i*22}H1190" stroke="#5e6ba5" stroke-opacity=".13"/>'
body += '<g font-family="Segoe UI,Arial,sans-serif"><text x="58" y="61" fill="#67e8f9" font-size="13" letter-spacing="4">P C T E J A  /  THE BUILD LOG</text>'
body += '<text x="55" y="160" fill="#f1f5ff" font-size="82" font-weight="800" letter-spacing="-4">TEJA P C<tspan fill="#67e8f9">.</tspan></text>'
body += '<text x="60" y="206" fill="url(#accent)" font-size="22" font-weight="600">Software engineering. AI. A little bit of chaos.</text>'
body += '<text x="60" y="242" fill="#a9b6d4" font-size="17">Building useful things, one curious commit at a time.</text>'
body += '<rect x="60" y="290" width="376" height="36" rx="18" fill="#0b152c" stroke="#314669"/><circle cx="81" cy="308" r="4" fill="#67e8f9"><animate attributeName="opacity" values="1;.3;1" dur="3s" repeatCount="indefinite"/></circle><text x="96" y="313" fill="#cbd5e1" font-size="12" letter-spacing="1.6">BUILD. BREAK. LEARN. REPEAT.</text></g>'
body += '<ellipse cx="966" cy="307" rx="98" ry="18" fill="#000" opacity=".25"><animate attributeName="rx" values="98;82;98" dur="6s" repeatCount="indefinite"/></ellipse>'
body += '<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -13;0 0" dur="6s" repeatCount="indefinite"/>'
body += '<polygon points="966,98 1078,160 966,225 854,160" fill="url(#top)" stroke="#c4b5fd"/><polygon points="854,160 966,225 966,299 854,234" fill="url(#left)"/><polygon points="966,225 1078,160 1078,234 966,299" fill="url(#right)"/>'
body += '<path d="M878 164l88 50 89-51 M966 226v53" fill="none" stroke="#c4b5fd" opacity=".45"/><text x="966" y="174" text-anchor="middle" font-family="monospace" font-size="37" fill="#172554" font-weight="bold">&lt;/&gt;</text></g>'
body += '<ellipse cx="966" cy="212" rx="168" ry="60" transform="rotate(-22 966 212)" fill="none" stroke="#67e8f9" stroke-opacity=".4" stroke-width="1.5" stroke-dasharray="6 10"><animate attributeName="stroke-dashoffset" from="0" to="96" dur="12s" repeatCount="indefinite"/></ellipse>'
for x,y,r,c in [(816,100,7,'#67e8f9'),(1104,277,5,'#c4b5fd'),(1067,70,3,'#e879f9'),(772,244,3,'#67e8f9')]:
    body += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"><animate attributeName="opacity" values=".9;.3;.9" dur="4s" repeatCount="indefinite"/></circle>'
save('hero.svg',1200,380,'Teja P C. Software engineering, AI, and a little bit of chaos. Animated floating 3D code cube.',body,defs)

icons = {
    'linkedin': '<rect x="14" y="13" width="24" height="24" rx="5" fill="#0a66c2"/><text x="18" y="31" fill="white" font-size="20" font-family="Arial" font-weight="bold">in</text>',
    'scholar': '<path d="M13 23l14-11 14 11-14 9z" fill="#60a5fa"/><circle cx="27" cy="30" r="8" fill="#93c5fd"/><path d="M16 21l11-9 11 9-11 8z" fill="#4285f4"/>',
    'portfolio': '<path d="M17 19l-6 6 6 6m17-12 6 6-6 6m-5-16-6 32" fill="none" stroke="#a78bfa" stroke-width="2.5" stroke-linecap="round"/>',
    'resume': '<rect x="17" y="12" width="20" height="27" rx="3" fill="none" stroke="#67e8f9" stroke-width="2"/><path d="M22 20h10m-10 6h10m-10 6h7" stroke="#67e8f9" stroke-width="2"/>',
    'coffee': '<path d="M15 19h20v12a8 8 0 0 1-8 8h-4a8 8 0 0 1-8-8z" fill="#facc15"/><path d="M35 21h3a5 5 0 0 1 0 10h-3M21 8v5m8-5v5" fill="none" stroke="#facc15" stroke-width="2"/>',
}
for name,label,w in [('linkedin','LinkedIn',144),('scholar','Google Scholar',193),('portfolio','3D Portfolio',174),('resume','Resume',142),('coffee','Buy me a coffee',200)]:
    body=f'<rect x="1" y="1" width="{w-2}" height="48" rx="12" fill="#10182c" stroke="#33415f"/><path d="M13 48h{w-26}" stroke="#818cf8" opacity=".6"/>{icons[name]}<text x="50" y="30" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="600" fill="#e2e8f0">{label}</text>'
    save(name+'.svg',w,50,label,body)

body='<rect width="1200" height="150" rx="22" fill="url(#bg)"/><path d="M0 1H1200" stroke="url(#accent)" stroke-width="3"/><g font-family="Segoe UI,Arial,sans-serif" text-anchor="middle"><text x="600" y="64" fill="#f1f5ff" font-size="26" font-weight="700">The models have GPUs. I have a mug.</text><text x="600" y="99" fill="#a5b4fc" font-size="17">We are both doing our best.</text></g>'
save('coffee-banner.svg',1200,150,'The models have GPUs. I have a mug. We are both doing our best.',body,defs)

body='<rect width="1200" height="148" rx="22" fill="#0b1020"/><g font-family="Segoe UI,Arial,sans-serif" text-anchor="middle">'
for x,val,label,col in [(200,'~$200K','PROJECTED API COST SAVINGS','#67e8f9'),(600,'70%','LESS MANUAL DATA ENTRY','#c4b5fd'),(1000,'10M+','RECORDS THROUGH DATA PIPELINES','#67e8f9')]:
    body+=f'<text x="{x}" y="76" fill="{col}" font-size="40" font-weight="700">{val}</text><text x="{x}" y="110" fill="#94a3b8" font-size="12" letter-spacing="1.3">{label}</text>'
body+='</g><path d="M400 32v85m400-85v85" stroke="#28344e"/>'
save('impact.svg',1200,148,'Selected career impact: nearly $200K projected API savings, 70% less manual entry, 10M+ records processed.',body)
for slug, number, title, lines, stack in [
    ('project-mcp','01','MCP, made visual',['An interactive guide to how AI','connects with tools and context.'],'HTML  /  CSS  /  JAVASCRIPT'),
    ('project-agents','02','Predict the next tool',['ML experiments with 12,000 tool traces:','cacheability, next tool, and latency.'],'PYTHON  /  MULTIMODAL ML'),
    ('project-portfolio','03','A portfolio with depth',['3D scenes, motion, and a little','extra personality per pixel.'],'REACT  /  THREE.JS'),
    ('project-solar','04','Forecast the sunshine',['A solar-power prediction interface','built around weather and plant data.'],'PYTHON  /  APPLIED ML'),
]:
    body=f'<rect x="1" y="1" width="578" height="208" rx="20" fill="#0b1020" stroke="#2b3858"/><path d="M22 1H150" stroke="#67e8f9" stroke-width="2"/><g font-family="Segoe UI,Arial,sans-serif"><text x="30" y="38" fill="#818cf8" font-size="12" letter-spacing="2">THE WORKSHOP / {number}</text><text x="548" y="41" fill="#67e8f9" font-size="23" text-anchor="end">↗</text><text x="30" y="80" fill="#e2e8f0" font-size="26" font-weight="700">{html.escape(title)}</text><text x="30" y="116" fill="#94a3b8" font-size="17">{html.escape(lines[0])}</text><text x="30" y="143" fill="#94a3b8" font-size="17">{html.escape(lines[1])}</text><text x="30" y="183" fill="#67e8f9" font-size="11" letter-spacing="1.4">{stack}</text></g>'
    save(slug+'.svg',580,210,title+'. '+' '.join(lines),body)
print('Created', len(list(OUT.glob('*.svg'))), 'custom profile assets.')
