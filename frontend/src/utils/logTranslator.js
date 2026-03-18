/**
 * Translates system dashboard log messages from Chinese to English
 * when the app is in English mode. Uses simple phrase mapping
 * rather than full i18n (these are operational console messages).
 */

const LOG_PHRASES = [
  // Status
  ['环境搭建完成，可以开始模拟', 'Environment setup complete, ready to simulate'],
  ['环境搭建初始化', 'environment setup initializing'],
  ['模拟实例已创建', 'Simulation instance created'],
  ['正在准备模拟环境', 'Preparing simulation environment'],
  ['检测到已有完成的准备工作，直接使用', 'Existing preparation found, reusing'],
  ['正在加载已有配置数据', 'Loading existing config data'],
  ['准备工作已完成', 'Preparation complete'],
  ['准备任务已启动', 'Preparation task started'],
  ['准备失败', 'Preparation failed'],
  ['准备异常', 'Preparation error'],
  ['开始轮询准备进度', 'Polling preparation progress'],
  ['配置生成中，开始轮询等待', 'Config generating, polling'],

  // Agent profiles
  ['开始生成Agent人设', 'Generating agent profiles'],
  ['正在生成Agent人设配置', 'Generating agent profile config'],
  ['Agent人设生成完成', 'agent profiles generated'],
  ['Agent人设', 'Agent profile'],
  ['已加载', 'Loaded'],
  ['个Agent人设', 'agent profiles'],
  ['未知职业', 'Unknown'],

  // Config
  ['开始生成双平台模拟配置', 'Generating dual-platform config'],
  ['正在调用LLM生成模拟配置参数', 'Calling LLM to generate simulation config'],
  ['模拟配置生成完成', 'Simulation config generated'],
  ['模拟配置加载成功', 'Simulation config loaded'],
  ['加载配置失败', 'Config load failed'],
  ['叙事方向', 'Narrative direction'],
  ['时间配置', 'Time config'],
  ['Agent数量', 'Agent count'],
  ['模拟时长', 'Duration'],
  ['初始帖子', 'Initial posts'],
  ['热点话题', 'Hot topics'],
  ['平台配置', 'Platform config'],

  // Simulation
  ['开始模拟，自定义轮数', 'Starting simulation, custom rounds'],
  ['开始模拟，使用自动配置轮数', 'Starting simulation, auto-config rounds'],
  ['自定义模拟轮数', 'Custom simulation rounds'],
  ['使用自动配置的模拟轮数', 'Using auto-configured rounds'],
  ['进入 Step', 'Entering Step'],
  ['返回 Step', 'Back to Step'],
  ['检测到模拟环境正在运行，正在关闭', 'Simulation env running, shutting down'],
  ['检测到模拟状态为运行中，正在停止', 'Simulation running, stopping'],
  ['正在关闭模拟环境', 'Closing simulation environment'],
  ['模拟环境已关闭', 'Simulation environment closed'],
  ['关闭模拟环境失败', 'Failed to close simulation env'],
  ['关闭模拟环境异常', 'Error closing simulation env'],
  ['模拟已强制停止', 'Simulation force-stopped'],
  ['强制停止失败', 'Force stop failed'],
  ['强制停止模拟失败', 'Failed to force stop simulation'],
  ['强制停止模拟异常', 'Error force-stopping simulation'],
  ['正在停止模拟进程', 'Stopping simulation process'],
  ['模拟已停止', 'Simulation stopped'],
  ['停止模拟失败', 'Failed to stop simulation'],
  ['检查模拟状态失败', 'Failed to check simulation status'],
  ['准备返回 Step 2，正在关闭模拟', 'Returning to Step 2, closing simulation'],

  // Data loading
  ['加载模拟数据', 'Loading simulation data'],
  ['加载模拟数据失败', 'Failed to load simulation data'],
  ['加载报告数据', 'Loading report data'],
  ['项目加载成功', 'Project loaded'],
  ['图谱数据加载成功', 'Graph data loaded'],
  ['图谱加载失败', 'Graph load failed'],
  ['获取报告信息失败', 'Failed to get report info'],
  ['获取时间配置失败，使用默认值', 'Time config failed, using default'],
  ['加载异常', 'Load error'],
  ['开启图谱实时刷新', 'Graph real-time refresh enabled'],
  ['停止图谱实时刷新', 'Graph real-time refresh stopped'],

  // Step3 simulation
  ['模拟引擎启动成功', 'Simulation engine started'],
  ['正在启动双平台并行模拟', 'Starting dual-platform parallel simulation'],
  ['已开启动态图谱更新模式', 'Dynamic graph update mode enabled'],
  ['设置最大模拟轮数', 'Max simulation rounds set to'],
  ['已清理旧的模拟日志，重新开始模拟', 'Old simulation logs cleared, restarting'],
  ['正在停止模拟', 'Stopping simulation'],
  ['模拟已停止', 'Simulation stopped'],
  ['停止失败', 'Stop failed'],
  ['停止异常', 'Stop error'],
  ['检测到所有平台模拟已结束', 'All platform simulations finished'],
  ['模拟已完成', 'Simulation complete'],
  ['报告生成请求已发送，请稍候', 'Report generation request sent, please wait'],
  ['正在启动报告生成', 'Starting report generation'],
  ['报告生成任务已启动', 'Report generation task started'],
  ['启动报告生成失败', 'Failed to start report generation'],
  ['启动报告生成异常', 'Report generation start error'],
  ['启动失败', 'Start failed'],
  ['启动异常', 'Start error'],
  ['Step3 模拟运行初始化', 'Step3 simulation initialized'],
  ['设置最大模拟rounds数', 'Max simulation rounds set to'],

  // Init
  ['SimulationView 初始化', 'SimulationView initialized'],
  ['SimulationRunView 初始化', 'SimulationRunView initialized'],
  ['ReportView 初始化', 'ReportView initialized'],
  ['InteractionView 初始化', 'InteractionView initialized'],

  // Report
  ['进入 Step 4: 报告生成', 'Entering Step 4: Report generation'],
  ['进入 Step 3: 开始模拟', 'Entering Step 3: Simulation'],

  // Units (apply last - shorter matches)
  ['从Zep图谱读取到', 'Read from Zep graph:'],
  ['实体类型', 'entity types'],
  ['个实体', 'entities'],
  ['分钟/轮', 'min/round'],
  ['分钟', 'min'],
  ['小时', 'hours'],
  ['轮', 'rounds'],
  ['个', ''],
  ['条', ''],
  ['错误：', 'Error:'],
  ['缺少', 'Missing'],
]

export function translateLog(msg, locale) {
  if (locale !== 'en') return msg
  let result = msg
  for (const [zh, en] of LOG_PHRASES) {
    result = result.replaceAll(zh, en)
  }
  return result
}
