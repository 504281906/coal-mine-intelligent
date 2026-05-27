# 煤矿智能化常态化运行管理系统

智能化煤矿评级系统前端，支持九大系统常态化运行月度评价、数据可视化与报告导出。

**在线访问：** https://504281906.github.io/coal-mine-intelligent/

---

## 项目概述

本系统用于煤矿智能化常态化运行的月度评价，涵盖九大核心系统（地质保障、信息基础设施、掘进、综采、主运输、辅助运输、综合保障、安全管控、生产经营管理）及基本要求模块，通过指标考核与扣分制对矿井进行综合评分。

## 页面导航

| 页面 | 文件 | 说明 |
|------|------|------|
| 首页 | `index.html` | 驾驶舱总览，雷达图 + 六宫格卡片 |
| 数据中心 | `data-center.html` | 九大系统运行状态一览 |
| 指标评价 | `eval-template.html` | 评价指标体系管理 |
| 巡检任务 | `inspection.html` | 巡检计划与记录 |
| 智能监控 | `monitoring.html` | 实时监控数据看板 |
| 评价报告 | `report.html` | 历史评价报告列表 |
| **报告打印版** | `report-print.html` | **A4 打印/PDF 导出专用版，含完整四章内容** |
| 整改管理 | `rectification.html` | 整改任务追踪 |

## 评分体系

- **总分：** 1000 分（九大系统 × 100分 + 基本要求 × 100分）
- **加分项：** 最高 +50 分
- **扣分制：** 按指标逐项扣分，记录扣分原因
- **评级：** 优秀（≥900）/ 良好（700-899）/ 合格（600-699）/ 不合格（<600）

## 九大系统

1. 基本要求
2. 信息基础设施
3. 地质保障系统
4. 掘进系统
5. 综采系统
6. 主运输系统
7. 辅助运输系统
8. 综合保障系统
9. 安全管控系统
10. 生产经营管理系统

## 技术栈

- 纯前端 HTML + CSS + JavaScript（无需构建）
- 雷达图：Canvas API 自主绘制
- 图标：Lucide Icons（CDN）
- 字体：PingFang SC / Microsoft YaHei
- 部署：GitHub Pages
- 打印支持：CSS `@media print` 适配 A4

## 文件结构

```
coal-mine-intelligent/
├── index.html          # 首页（驾驶舱）
├── data-center.html   # 数据中心
├── eval-template.html # 指标评价
├── inspection.html    # 巡检任务
├── monitoring.html   # 智能监控
├── report.html       # 评价报告列表
├── report-print.html # 报告打印版 ★
├── rectification.html # 整改管理
└── README.md
```

## 本地预览

直接用浏览器打开 HTML 文件，或：

```bash
npx serve .
```

## 相关说明

- 报告打印版 (`report-print.html`) 已集成打印样式，浏览器打印时自动隐藏侧边栏和顶部栏，全宽 A4 布局
- 所有页面共用统一设计规范（CSS 变量体系），侧边栏导航结构一致
- 数据均为示例数据，真实场景请替换为实际矿井数据