"""
Backend i18n dictionary for fixed Chinese strings.
These are error/status messages hardcoded in route handlers and services.
Looked up locally (zero cost) before falling through to the translation API.
"""

# Chinese → English mapping for all fixed backend strings
ZH_EN = {
    # ── graph.py ──
    "项目不存在": "Project does not exist",
    "项目不存在或删除失败": "Project does not exist or deletion failed",
    "项目已删除": "Project deleted",
    "项目已重置": "Project reset",
    "请提供模拟需求描述 (simulation_requirement)": "Please provide a simulation requirement",
    "请至少上传一个文档文件": "Please upload at least one document file",
    "没有成功处理任何文档，请检查文件格式": "No documents processed successfully. Please check the file format.",
    "请提供 project_id": "Please provide project_id",
    "项目尚未生成本体，请先调用 /ontology/generate": "Ontology not yet generated. Please call /ontology/generate first.",
    "图谱正在构建中，请勿重复提交。如需强制重建，请添加 force: true": "Graph is being built. Do not resubmit. To force rebuild, add force: true.",
    "未找到提取的文本内容": "Extracted text content not found",
    "未找到本体定义": "Ontology definition not found",
    "图谱构建任务已启动": "Graph build task started",
    "图谱构建任务已启动，请通过 /task/{task_id} 查询进度": "Graph build task started. Query progress via /task/{task_id}.",
    "任务不存在": "Task does not exist",
    "ZEP_API_KEY未配置": "ZEP_API_KEY not configured",
    "图谱已删除": "Graph deleted",
    "配置错误": "Configuration error",

    # ── graph.py task messages ──
    "初始化图谱构建服务...": "Initializing graph build service...",
    "文本分块中...": "Chunking text...",
    "创建Zep图谱...": "Creating Zep graph...",
    "设置本体定义...": "Setting ontology definition...",
    "等待Zep处理数据...": "Waiting for Zep to process data...",
    "获取图谱数据...": "Fetching graph data...",
    "图谱构建完成": "Graph build complete",
    "构建失败": "Build failed",

    # ── simulation.py ──
    "请提供 simulation_id": "Please provide simulation_id",
    "请提供 agent_id": "Please provide agent_id",
    "请提供 prompt（采访问题）": "Please provide a prompt (interview question)",
    "请提供 interviews（采访列表）": "Please provide interviews list",
    "项目尚未构建图谱，请先调用 /api/graph/build": "Graph not yet built. Please call /api/graph/build first.",
    "准备任务已启动": "Preparation task started",
    "已有完成的准备工作，无需重复生成": "Existing preparation found, no need to regenerate",
    "已有完成的准备工作": "Existing preparation found",
    "项目缺少模拟需求描述 (simulation_requirement)": "Project missing simulation requirement",
    "准备任务已启动，请通过 /api/simulation/prepare/status 查询进度": "Preparation started. Query progress via /api/simulation/prepare/status.",
    "尚未开始准备，请调用 /api/simulation/prepare 开始": "Preparation not started. Call /api/simulation/prepare to begin.",
    "请提供 task_id 或 simulation_id": "Please provide task_id or simulation_id",
    "任务已完成（准备工作已存在）": "Task completed (preparation already exists)",
    "配置文件不存在，请先调用 /prepare 接口": "Config file does not exist. Call /prepare first.",
    "请提供 graph_id": "Please provide graph_id",
    "没有找到符合条件的实体": "No matching entities found",
    "模拟环境未运行或已关闭。请确保模拟已完成并进入等待命令模式。": "Simulation environment not running or closed. Ensure the simulation has completed and entered command mode.",
    "启用图谱记忆更新需要有效的 graph_id，请确保项目已构建图谱": "Graph memory update requires a valid graph_id. Ensure the graph has been built.",
    "数据库不存在，模拟可能尚未运行": "Database does not exist. Simulation may not have run yet.",
    "环境正在运行，可以接收Interview命令": "Environment is running and ready for Interview commands",
    "环境关闭命令已发送": "Environment shutdown command sent",

    # ── report.py ──
    "请提供 message": "Please provide a message",
    "报告已存在": "Report already exists",
    "报告已生成": "Report already generated",
    "报告生成任务已启动": "Report generation task started",
    "报告生成任务已启动，请通过 /api/report/generate/status 查询进度": "Report generation started. Query progress via /api/report/generate/status.",
    "缺少图谱ID，请确保已构建图谱": "Missing graph ID. Ensure the graph has been built.",
    "缺少图谱ID": "Missing graph ID",
    "缺少模拟需求描述": "Missing simulation requirement",
    "请提供 graph_id 和 query": "Please provide graph_id and query",
    "报告不存在": "Report does not exist",
    "该模拟暂无报告": "No report for this simulation yet",
    "章节不存在": "Section does not exist",
    "报告不存在或进度信息不可用": "Report does not exist or progress unavailable",
    "报告已删除": "Report deleted",

    # ── report_agent.py ──
    "报告生成任务开始": "Report generation task started",
    "开始规划报告大纲": "Starting report outline planning",
    "获取模拟上下文信息": "Fetching simulation context",
    "大纲规划完成": "Outline planning complete",
    "报告生成完成": "Report generation complete",
    "报告生成失败": "Report generation failed",

    # ── simulation_runner.py ──
    "模拟目录不存在，无需清理": "Simulation directory does not exist, no cleanup needed",

    # ── common patterns (partial matches handled by startswith) ──
    "模拟不存在": "Simulation does not exist",
    "项目不存在": "Project does not exist",
}


import re

# Regex-based patterns for dynamic progress messages
_REGEX_PATTERNS = [
    (re.compile(r'^发送第 (\d+)/(\d+) 批数据 \((\d+) 块\)'), r'Sending batch \1/\2 (\3 chunks)...'),
    (re.compile(r'^批次 (\d+) 发送失败'), r'Batch \1 send failed'),
    (re.compile(r'^开始等待 (\d+) 个文本块处理'), r'Waiting for \1 text chunks to process...'),
    (re.compile(r'^部分文本块超时，已完成 (\d+)/(\d+)'), r'Some chunks timed out, completed \1/\2'),
    (re.compile(r'^Zep处理中\.\.\. (\d+)/(\d+) 完成, (\d+) 待处理 \((\d+)秒\)'), r'Zep processing... \1/\2 done, \3 pending (\4s)'),
    (re.compile(r'^处理完成: (\d+)/(\d+)'), r'Processing complete: \1/\2'),
    (re.compile(r'^图谱已创建'), 'Graph created'),
    (re.compile(r'^文本已分割为 (\d+) 个块'), r'Text split into \1 chunks'),
    (re.compile(r'^构建失败'), 'Build failed'),
]


def lookup(text):
    """
    Try to translate a fixed backend string locally.
    Returns English translation or None if not in the dictionary.
    """
    if not text:
        return None

    # Exact match
    if text in ZH_EN:
        return ZH_EN[text]

    # Prefix match: "Chinese prefix: dynamic_value"
    for zh, en in ZH_EN.items():
        if text.startswith(zh) and len(text) > len(zh):
            suffix = text[len(zh):]
            return en + suffix

    # Regex match: dynamic progress messages
    for pattern, replacement in _REGEX_PATTERNS:
        match = pattern.match(text)
        if match:
            return match.expand(replacement)

    return None
