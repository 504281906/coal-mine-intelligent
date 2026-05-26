import os

BASE = '/root/.openclaw/workspace/coal-mine-system/docs'
d = open(BASE + '/dashboard.html').read()
css_full = d[d.index('<style>')+7:d.index('</style>')]

SIDEBAR = [
    ('home','index.html','首页'),
    ('database','data-center.html','数据中心'),
    ('bar-chart-2','eval-template.html','指标评价'),
    ('clipboard-list','inspection.html','巡检任务'),
    ('monitor','monitoring.html','智能监控'),
    ('file-text','report.html','评价报告'),
    ('check-circle','rectification.html','整改管理'),
]
ICONS = {
    'home':'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"></path><path d="M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>',
    'database':'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path></svg>',
    'bar-chart-2':'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><path d="M5 21v-6"></path><path d="M12 21V3"></path><path d="M19 21V9"></path></svg>',
    'clipboard-list':'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"></rect><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><path d="M12 11h4"></path><path d="M12 16h4"></path><path d="M8 11h.01"></path><path d="M8 16h.01"></path></svg>',
    'monitor':'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><rect width="20" height="14" x="2" y="3" rx="2"></rect><line x1="8" x2="16" y1="21" y2="21"></line><line x1="12" x2="12" y1="17" y2="21"></line></svg>',
    'file-text':'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"></path><path d="M14 2v5a1 1 0 0 0 1 1h5"></path><path d="M10 9H8"></path><path d="M16 13H8"></path><path d="M16 17H8"></path></svg>',
    'check-circle':'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>',
}
LOGO_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:16px;height:16px;"><path d="M12 10h.01"></path><path d="M12 14h.01"></path><path d="M12 6h.01"></path><path d="M16 10h.01"></path><path d="M16 14h.01"></path><path d="M16 6h.01"></path><path d="M8 10h.01"></path><path d="M8 14h.01"></path><path d="M8 6h.01"></path><path d="M9 22v-3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3"></path><rect x="4" y="2" width="16" height="20" rx="2"></rect></svg>'

EXTRA = """
.kpi-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px;display:flex;flex-direction:column;gap:4px;transition:box-shadow 0.2s;}
.kpi-card:hover{box-shadow:0 4px 16px rgba(0,0,0,0.08);}
.kpi-label{font-size:11px;color:var(--text-muted);font-weight:600;text-transform:uppercase;letter-spacing:0.5px;}
.kpi-value{font-size:32px;font-weight:800;line-height:1;}
.kpi-unit{font-size:14px;font-weight:400;color:var(--text-muted);margin-left:2px;}
.kpi-delta{font-size:11px;font-weight:700;margin-left:6px;}
.kpi-delta.up{color:var(--accent-green);}
.kpi-delta.down{color:var(--accent-red);}
.kpi-sub{font-size:11px;color:var(--text-muted);margin-top:2px;}
.mod-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:14px;display:flex;flex-direction:column;gap:8px;cursor:pointer;transition:all 0.2s;}
.mod-card:hover{box-shadow:0 4px 16px rgba(0,0,0,0.10);border-color:var(--accent-blue);transform:translateY(-1px);}
.mod-card .mod-icon{width:34px;height:34px;border-radius:9px;display:flex;align-items:center;justify-content:center;}
.mod-title{font-size:12px;font-weight:700;color:var(--text-primary);}
.mod-desc{font-size:11px;color:var(--text-muted);line-height:1.4;}
.section-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
.section-title{font-size:14px;font-weight:700;color:var(--text-primary);display:flex;align-items:center;gap:8px;}
.section-title .dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.section-more{font-size:11px;color:var(--accent-blue);cursor:pointer;}
.section-more:hover{text-decoration:underline;}
.sys-dot-wrap{display:flex;flex-direction:column;align-items:center;gap:6px;padding:12px 6px;background:var(--bg-card);border:1px solid var(--border);border-radius:10px;transition:all 0.2s;cursor:pointer;}
.sys-dot-wrap:hover{box-shadow:0 2px 8px rgba(0,0,0,0.08);border-color:var(--accent-blue);}
.sys-dot-name{font-size:10px;color:var(--text-secondary);text-align:center;font-weight:500;}
.sys-dot-lamp{width:10px;height:10px;border-radius:50%;flex-shrink:0;}
.sys-dot-lamp.online{background:var(--accent-green);box-shadow:0 0 0 3px rgba(22,163,74,0.15);}
.sys-dot-lamp.warn{background:var(--accent-amber);box-shadow:0 0 0 3px rgba(217,119,6,0.15);animation:pulse-warn 2s infinite;}
.sys-dot-lamp.offline{background:var(--accent-red);box-shadow:0 0 0 3px rgba(220,38,38,0.15);}
@keyframes pulse-warn{0%,100%{opacity:1;}50%{opacity:0.5;}}
.alert-item{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;border-radius:8px;}
.alert-item.critical{border:1px solid #fecaca;background:#fef2f2;}
.alert-item.warning{border:1px solid #fde68a;background:#fef9ec;}
.alert-level{font-size:10px;font-weight:700;padding:2px 6px;border-radius:4px;flex-shrink:0;}
.alert-level.critical{background:var(--accent-red);color:#fff;}
.alert-level.warning{background:var(--accent-amber);color:#fff;}
.alert-title{font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:2px;}
.alert-meta{font-size:11px;color:var(--text-muted);}
.tag{display:inline-block;padding:2px 8px;border-radius:6px;font-size:11px;font-weight:600;}
.tag.ok{background:rgba(22,163,74,0.1);color:var(--accent-green);}
.tag.warn{background:rgba(220,38,38,0.1);color:var(--accent-red);}
.tag.info{background:rgba(37,99,235,0.1);color:var(--accent-blue);}
.tag.amber{background:rgba(217,119,6,0.1);color:var(--accent-amber);}
.blue-link{color:var(--accent-blue);cursor:pointer;text-decoration:none;}
.blue-link:hover{text-decoration:underline;}
.rank-item{display:flex;align-items:center;gap:8px;padding:7px 10px;background:#f5f7fa;border-radius:7px;}
.rank-num{font-size:10px;font-weight:800;color:var(--text-muted);width:14px;text-align:center;flex-shrink:0;}
.rank-num.top{color:var(--accent-amber);}
.rank-name{flex:1;font-size:11px;color:var(--text-secondary);}
.rank-bar{flex:1;height:5px;background:#dde1e7;border-radius:3px;overflow:hidden;}
.rank-bar-fill{height:100%;border-radius:3px;}
.score-badge{display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:13px;font-size:22px;font-weight:800;flex-shrink:0;}
.score-badge.excellent{background:rgba(22,163,74,0.1);color:var(--accent-green);}
.score-badge.good{background:rgba(37,99,235,0.1);color:var(--accent-blue);}
.score-badge.fail{background:rgba(220,38,38,0.1);color:var(--accent-red);}
.score-badge.amber{background:rgba(217,119,6,0.1);color:var(--accent-amber);}
"""

def make_html(body_content):
    sb = ''.join(['<a class="sidebar-item'+(' active' if k=='home' else '')+'" href="'+href+'"><div class="icon">'+ICONS[k]+'</div><span>'+label+'</span></a>' for k,href,label in SIDEBAR])
    return ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>煤矿智能化常态化运行管理系统</title>'
            '<script src="https://unpkg.com/lucide@latest"></script>'
            '<style>'+css_full+EXTRA+'</style></head><body>'
            '<div class="header"><div class="logo"><div class="logo-icon">'+LOGO_SVG+'</div>煤矿智能化常态化运行管理系统</div>'
            '<div class="header-right"><div class="header-time" id="clock">--:--:--</div><div class="header-user">王矿长</div></div></div>'
            '<div class="main-wrapper"><div class="sidebar">'+sb+'</div><div class="content">'+body_content+'</div></div>'
            '<script>function updateClock(){var n=new Date(),e=document.getElementById("clock");if(e)e.textContent=String(n.getHours()).padStart(2,"0")+":"+String(n.getMinutes()).padStart(2,"0")+":"+String(n.getSeconds()).padStart(2,"0");}setInterval(updateClock,1e3);updateClock();if(typeof lucide!=="undefined")lucide.createIcons();</script>'
            '</body></html>')

SYSTEMS = [
    ('综采系统','online'),('掘进系统','warn'),('主运输系统','online'),('辅助运输','online'),
    ('地质保障','online'),('通风系统','online'),('排水系统','warn'),('供电系统','online'),
    ('压风系统','online'),('信息基础','online'),
]
RANKS = [
    ('1','主运输系统',92,'var(--accent-green)'),('2','综采系统',85,'var(--accent-green)'),
    ('3','压风系统',78,'var(--accent-green)'),('4','掘进系统',72,'var(--accent-blue)'),
    ('5','通风系统',68,'var(--accent-blue)'),('6','供电系统',65,'var(--accent-blue)'),
    ('7','排水系统',58,'var(--accent-amber)'),('8','地质保障',42,'var(--accent-red)'),
]

rank_html = ''
for i,(rank,name,score,color) in enumerate(RANKS):
    top='top' if i<3 else ''
    rank_html += f'<div class="rank-item"><span class="rank-num {top}">{rank}</span><span class="rank-name">{name}</span><div class="rank-bar"><div class="rank-bar-fill" style="width:{score}%;background:{color};"></div></div><span style="font-size:11px;font-weight:700;color:{color};">{score}</span></div>\n'

sys_html = ''
for name,status in SYSTEMS:
    sys_html += f'<div class="sys-dot-wrap"><div class="sys-dot-lamp {status}"></div><div class="sys-dot-name">{name}</div></div>\n'

body = f"""
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
  <div>
    <div style="font-size:18px;font-weight:800;color:var(--text-primary);">数据总览</div>
    <div style="font-size:12px;color:var(--text-muted);margin-top:2px;">2026年05月 &middot; Intelligent Coal Mine</div>
  </div>
  <div style="display:flex;align-items:center;gap:10px;">
    <div style="font-size:11px;color:var(--text-muted);display:flex;align-items:center;gap:6px;">
      <span style="width:7px;height:7px;border-radius:50%;background:var(--accent-green);animation:pulse-warn 2s infinite;display:inline-block;"></span>
      数据采集中 &middot; 实时更新
    </div>
    <button class="btn primary" onclick="location.reload()" style="font-size:12px;padding:6px 14px;">刷新</button>
  </div>
</div>

<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px;">
  <div class="kpi-card">
    <div class="kpi-label">综合得分</div>
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span class="kpi-value" style="color:var(--accent-blue);">72</span>
      <span class="kpi-unit">分</span>
      <span class="kpi-delta up">&#9650; +5</span>
    </div>
    <div class="kpi-sub">较上月 &#8593;5分 &middot; 等级：合格</div>
    <div style="margin-top:8px;display:flex;align-items:center;gap:8px;">
      <span class="tag ok">合格</span><span class="tag info">良好</span>
    </div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">子系统状态</div>
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span class="kpi-value" style="color:var(--accent-green);">8</span>
      <span class="kpi-unit">/ 8 在线</span>
    </div>
    <div class="kpi-sub">本月无人值守率 <strong style="color:var(--accent-blue);">85%</strong></div>
    <div style="margin-top:8px;display:flex;gap:8px;">
      <span style="font-size:11px;color:var(--accent-green);display:flex;align-items:center;gap:4px;"><span style="width:7px;height:7px;border-radius:50%;background:var(--accent-green);flex-shrink:0;"></span>正常 6</span>
      <span style="font-size:11px;color:var(--accent-amber);display:flex;align-items:center;gap:4px;"><span style="width:7px;height:7px;border-radius:50%;background:var(--accent-amber);flex-shrink:0;"></span>告警 2</span>
    </div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">巡检任务</div>
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span class="kpi-value" style="color:var(--accent-amber);">12</span>
      <span class="kpi-unit">条待处理</span>
    </div>
    <div class="kpi-sub">进行中 5 &middot; 已超时 3 &middot; 今日新增 8</div>
    <div style="margin-top:8px;">
      <div style="height:4px;background:#e8ecf0;border-radius:2px;overflow:hidden;"><div style="height:100%;width:68%;background:var(--accent-green);border-radius:2px;"></div></div>
      <div style="font-size:10px;color:var(--text-muted);margin-top:3px;">完成率 68%</div>
    </div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">整改任务</div>
    <div style="display:flex;align-items:baseline;gap:3px;">
      <span class="kpi-value" style="color:var(--accent-red);">5</span>
      <span class="kpi-unit">条超期</span>
    </div>
    <div class="kpi-sub">本月整改完成率 <strong style="color:var(--accent-green);">76%</strong></div>
    <div style="margin-top:8px;font-size:11px;color:var(--text-muted);">待整改 9 &middot; 已完成 28</div>
  </div>
</div>

<div style="margin-bottom:16px;">
  <div class="section-header">
    <div class="section-title"><span class="dot" style="background:var(--accent-blue);"></span>功能模块</div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:10px;">
    <div class="mod-card" onclick="location.href='data-center.html'">
      <div class="mod-icon" style="background:rgba(37,99,235,0.1);color:var(--accent-blue);">&#128452;</div>
      <div class="mod-title">运行数据中心</div>
      <div class="mod-desc">数据源接入 &middot; 采集配置</div>
    </div>
    <div class="mod-card" onclick="location.href='eval-template.html'">
      <div class="mod-icon" style="background:rgba(22,163,74,0.1);color:var(--accent-green);">&#128202;</div>
      <div class="mod-title">指标评价中心</div>
      <div class="mod-desc">模板定义 &middot; 权重配置</div>
    </div>
    <div class="mod-card" onclick="location.href='inspection.html'">
      <div class="mod-icon" style="background:rgba(217,119,6,0.1);color:var(--accent-amber);">&#128203;</div>
      <div class="mod-title">巡检任务中心</div>
      <div class="mod-desc">任务派发 &middot; 执行追踪</div>
    </div>
    <div class="mod-card" onclick="location.href='monitoring.html'">
      <div class="mod-icon" style="background:rgba(147,51,234,0.1);color:#9333ea;">&#128200;</div>
      <div class="mod-title">智能监控中心</div>
      <div class="mod-desc">实时监控 &middot; 远程控制</div>
    </div>
    <div class="mod-card" onclick="location.href='report.html'">
      <div class="mod-icon" style="background:rgba(37,99,235,0.08);color:var(--accent-blue);">&#128196;</div>
      <div class="mod-title">评价报告中心</div>
      <div class="mod-desc">评分计算 &middot; 报告生成</div>
    </div>
    <div class="mod-card" onclick="location.href='rectification.html'">
      <div class="mod-icon" style="background:rgba(220,38,38,0.1);color:var(--accent-red);">&#10004;</div>
      <div class="mod-title">整改管理中心</div>
      <div class="mod-desc">任务派发 &middot; 验收闭环</div>
    </div>
    <div class="mod-card" onclick="location.href='settings.html'">
      <div class="mod-icon" style="background:rgba(90,100,117,0.1);color:var(--text-secondary);">&#9881;</div>
      <div class="mod-title">系统设置</div>
      <div class="mod-desc">参数配置 &middot; 权限管理</div>
    </div>
  </div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:16px;">
  <div class="card">
    <div class="card-header">
      <div class="card-title"><span class="card-dot" style="background:var(--accent-blue);"></span>最新评价报告</div>
      <span class="blue-link section-more" onclick="location.href='report.html'">查看全部 &rarr;</span>
    </div>
    <div style="display:flex;align-items:center;gap:14px;padding:14px 16px;background:#f5f7fa;border-radius:10px;border:1px solid var(--border);margin-bottom:14px;">
      <div class="score-badge good">72</div>
      <div style="flex:1;">
        <div style="font-size:13px;font-weight:700;color:var(--text-primary);margin-bottom:3px;">2026年05月 &middot; 智能化系统月度评价</div>
        <div style="font-size:11px;color:var(--text-muted);margin-bottom:6px;">2026-05-26 10:00 &nbsp;|&nbsp; 月度评价</div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;">
          <span class="tag ok">合格</span><span class="tag info">良好</span>
          <span style="font-size:11px;color:var(--text-muted);">良好（&ge;70分）</span>
        </div>
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;align-items:flex-end;">
        <span style="font-size:10px;color:var(--text-muted);">更新时间</span>
        <span style="font-size:11px;font-weight:600;color:var(--text-secondary);">今天 10:00</span>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:6px;">
{rank_html}    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <div class="card-title"><span class="card-dot" style="background:var(--accent-purple);"></span>子系统运行状态</div>
      <span class="blue-link section-more" onclick="location.href='monitoring.html'">查看全部 &rarr;</span>
    </div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:14px;">
{sys_html}    </div>
    <div style="display:flex;flex-direction:column;gap:8px;">
      <div class="alert-item critical">
        <div class="alert-level critical">高压</div>
        <div class="alert-content"><div class="alert-title">排水系统 - 1号排水泵温度异常</div><div class="alert-meta">2026-05-26 10:23 &middot; 持续 12 分钟</div></div>
      </div>
      <div class="alert-item warning">
        <div class="alert-level warning">中压</div>
        <div class="alert-content"><div class="alert-title">掘进系统 - TBM掘进速度低于阈值</div><div class="alert-meta">2026-05-26 09:45 &middot; 持续 50 分钟</div></div>
      </div>
    </div>
  </div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
  <div class="card">
    <div class="card-header">
      <div class="card-title"><span class="card-dot" style="background:var(--accent-amber);"></span>巡检任务动态</div>
      <span class="blue-link section-more" onclick="location.href='inspection.html'">查看全部 &rarr;</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:8px;">
      <div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:#f5f7fa;border-radius:8px;border:1px solid var(--border);">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(220,38,38,0.1);display:flex;align-items:center;justify-content:center;font-size:14px;">&#9888;</div>
        <div style="flex:1;">
          <div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:2px;">综采系统数据采集 &middot; 已超时 3 天</div>
          <div style="font-size:11px;color:var(--text-muted);">负责人：张志远 &middot; 应完成 2026-05-23</div>
        </div>
        <span class="tag warn">已超时</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:#f5f7fa;border-radius:8px;border:1px solid var(--border);">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(217,119,6,0.1);display:flex;align-items:center;justify-content:center;font-size:14px;">&#127919;</div>
        <div style="flex:1;">
          <div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:2px;">掘进系统巡检任务 &middot; 进行中</div>
          <div style="font-size:11px;color:var(--text-muted);">负责人：李建明 &middot; 进行中 40%</div>
        </div>
        <span class="tag amber">进行中</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:#f5f7fa;border-radius:8px;border:1px solid var(--border);">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(22,163,74,0.1);display:flex;align-items:center;justify-content:center;font-size:14px;">&#10004;</div>
        <div style="flex:1;">
          <div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:2px;">主运输系统月度巡检 &middot; 已完成</div>
          <div style="font-size:11px;color:var(--text-muted);">负责人：王海涛 &middot; 完成于 2026-05-25</div>
        </div>
        <span class="tag ok">已完成</span>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <div class="card-title"><span class="card-dot" style="background:var(--accent-red);"></span>整改任务动态</div>
      <span class="blue-link section-more" onclick="location.href='rectification.html'">查看全部 &rarr;</span>
    </div>
    <div style="display:flex;flex-direction:column;gap:8px;">
      <div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:#fef2f2;border-radius:8px;border:1px solid #fecaca;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(220,38,38,0.15);display:flex;align-items:center;justify-content:center;font-size:14px;">&#9888;</div>
        <div style="flex:1;">
          <div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:2px;">地质保障系统评分不达标 &middot; 超期</div>
          <div style="font-size:11px;color:var(--text-muted);">负责人：赵志强 &middot; 整改期限 2026-05-20</div>
        </div>
        <span class="tag warn">超期</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:#fef9ec;border-radius:8px;border:1px solid #fde68a;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(217,119,6,0.15);display:flex;align-items:center;justify-content:center;font-size:14px;">&#127919;</div>
        <div style="flex:1;">
          <div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:2px;">排水系统评分不达标 &middot; 整改中</div>
          <div style="font-size:11px;color:var(--text-muted);">负责人：钱伟民 &middot; 整改期限 2026-05-30</div>
        </div>
        <span class="tag amber">整改中</span>
      </div>
      <div style="display:flex;align-items:center;gap:10px;padding:10px 12px;background:#f0fdf4;border-radius:8px;border:1px solid #bbf7d0;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(22,163,74,0.15);display:flex;align-items:center;justify-content:center;font-size:14px;">&#10004;</div>
        <div style="flex:1;">
          <div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:2px;">掘进系统评分不达标 &middot; 待验收</div>
          <div style="font-size:11px;color:var(--text-muted);">负责人：孙晓峰 &middot; 完成于 2026-05-24</div>
        </div>
        <span class="tag info">待验收</span>
      </div>
    </div>
  </div>
</div>
"""

html = make_html(body)
open(BASE + '/index.html', 'w').write(html)
print('Done:', len(html), 'bytes')
