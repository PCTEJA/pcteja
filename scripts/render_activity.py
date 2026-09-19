"""Render public contribution activity. Uses only the repository's GitHub token."""

import datetime as dt
import html
import json
import os
from pathlib import Path
import urllib.request

USER = os.environ.get('PROFILE_USER', 'PCTEJA')
QUERY = '''query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}'''


def svg(width, height, title, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{html.escape(title)}">
    <title>{html.escape(title)}</title>
    <defs><linearGradient id="line" x1="0" x2="1"><stop stop-color="#22d3ee"/><stop offset="1" stop-color="#a78bfa"/></linearGradient>
    <linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#22d3ee" stop-opacity=".35"/><stop offset="1" stop-color="#a78bfa" stop-opacity="0"/></linearGradient></defs>
    <rect width="{width}" height="{height}" rx="20" fill="#0b1020"/>
    <g font-family="Segoe UI,Arial,sans-serif">{content}</g></svg>'''


def main():
    request = urllib.request.Request('https://api.github.com/graphql',
        data=json.dumps({'query': QUERY, 'variables': {'login': USER}}).encode(),
        headers={'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'],
                 'Content-Type': 'application/json', 'User-Agent': 'profile-visuals'})
    with urllib.request.urlopen(request, timeout=45) as response:
        result = json.load(response)
    if result.get('errors'):
        raise RuntimeError('GitHub contribution query failed: ' + json.dumps(result['errors']))
    calendar = result['data']['user']['contributionsCollection']['contributionCalendar']
    today = dt.datetime.now(dt.timezone.utc).date()
    days = [d for w in calendar['weeks'] for d in w['contributionDays'] if dt.date.fromisoformat(d['date']) <= today]
    if not days:
        raise RuntimeError('No contribution dates returned')
    counts = [d['contributionCount'] for d in days]
    longest = run = 0
    for count in counts:
        run = run + 1 if count else 0
        longest = max(longest, run)
    # A day still in progress does not break yesterday's streak.
    tail = counts[:-1] if days[-1]['date'] == today.isoformat() and counts[-1] == 0 else counts
    current = 0
    for count in reversed(tail):
        if not count:
            break
        current += 1
    total = sum(counts)
    active = sum(c > 0 for c in counts)
    caption = f"{days[0]['date']} to {days[-1]['date']} · UTC · public contribution calendar"
    cards = ''
    for x, number, label, color in [(130, f'{total:,}', 'CONTRIBUTIONS', '#67e8f9'),
                                    (390, str(current), 'CURRENT STREAK / DAYS', '#c4b5fd'),
                                    (650, str(longest), 'LONGEST IN WINDOW / DAYS', '#67e8f9')]:
        cards += f'<text x="{x}" y="83" text-anchor="middle" font-size="42" font-weight="700" fill="{color}">{number}</text><text x="{x}" y="111" text-anchor="middle" font-size="10" letter-spacing="1.2" fill="#94a3b8">{label}</text>'
    cards += '<path d="M260 38V120 M520 38V120" stroke="#24304a"/>'
    cards += f'<text x="390" y="151" text-anchor="middle" font-size="10" fill="#94a3b8">{caption}</text>'
    out = Path('profile')
    out.mkdir(exist_ok=True)
    (out / 'streak.svg').write_text(svg(780, 174, f'{USER}: {total} contributions, current streak {current} days, longest {longest} days in displayed window', cards), encoding='utf-8')
    recent = days[-90:]
    peak = max(1, max(d['contributionCount'] for d in recent))
    left, right, top, bottom = 55, 747, 84, 242
    points = [(left + i*(right-left)/max(1,len(recent)-1), bottom-d['contributionCount']/peak*(bottom-top)) for i,d in enumerate(recent)]
    path = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x,y in points)
    chart = '<text x="32" y="37" fill="#67e8f9" font-size="20" font-weight="600">The commit heartbeat</text>'
    chart += f'<text x="32" y="58" fill="#94a3b8" font-size="11">90 days of contributions · {active} active days in the full calendar</text>'
    for i in range(5):
        y = bottom - i*(bottom-top)/4
        chart += f'<path d="M{left} {y}H{right}" stroke="#1e2942"/><text x="42" y="{y+4}" text-anchor="end" fill="#64748b" font-size="10">{round(peak*i/4)}</text>'
    chart += f'<path d="{path} L{right},{bottom} L{left},{bottom} Z" fill="url(#area)"/>'
    chart += f'<path d="{path}" fill="none" stroke="url(#line)" stroke-width="2.5" stroke-linejoin="round"/>'
    x,y=points[-1]
    chart += f'<circle cx="{x}" cy="{y}" r="4" fill="#c4b5fd"><animate attributeName="opacity" values="1;.3;1" dur="3s" repeatCount="indefinite"/></circle>'
    chart += f'<text x="{left}" y="267" fill="#94a3b8" font-size="11">{recent[0]["date"]}</text><text x="{right}" y="267" text-anchor="end" fill="#94a3b8" font-size="11">{recent[-1]["date"]} · UTC</text>'
    (out / 'activity.svg').write_text(svg(780, 290, f'{USER} contribution activity over the last 90 days', chart), encoding='utf-8')
    print('Rendered activity and streak from', len(days), 'calendar days.')


if __name__ == '__main__':
    main()
