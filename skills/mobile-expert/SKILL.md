---
name: mobile-expert
description: >
  移动端专家技能。React Native、iOS、Android开发最佳实践，移动端性能优化。
  触发关键词：React Native、移动端、iOS、Android、小程序、App开发
version: 1.0.0
source_refs:
  - https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-native-guidelines/SKILL.md
agent_type: mobile
capabilities: [react-native, ios, android, mobile-performance, cross-platform]
---

# 移动端专家 Skill

## React Native 最佳实践

获取最新 Vercel React Native 指南：
```
fetch: https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-native-guidelines/SKILL.md
```

## 核心规范

### 性能优化
- 使用 `FlatList` 代替 `ScrollView`（大列表必须）
- `React.memo` 防止不必要重渲染
- 图片使用 `FastImage` 缓存
- 避免在渲染函数中创建对象/函数
- 使用 `useCallback`/`useMemo` 稳定引用

### 导航（React Navigation）
```javascript
// 类型安全的导航
type RootStackParams = {
  Home: undefined;
  Detail: { id: string };
};
```

### 样式规范
- 使用 `StyleSheet.create()` 性能优于内联样式
- 避免硬编码像素值，使用 `Dimensions` 或 `%`
- 适配安全区域：`SafeAreaView`
- 适配不同屏幕密度：`PixelRatio`

### 平台差异处理
```javascript
import { Platform } from 'react-native';

const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.OS === 'ios' ? 44 : 24,
  },
});
```

### 状态管理
- 简单状态：`useState` + `useContext`
- 复杂状态：Zustand（轻量）或 Redux Toolkit
- 服务端状态：React Query / TanStack Query

## 常见问题排查

| 问题 | 原因 | 解决 |
|------|------|------|
| 卡顿 | JS线程阻塞 | 使用Reanimated/Worklets |
| 内存泄漏 | 未清理监听器 | useEffect cleanup |
| 键盘遮挡 | 未处理键盘 | KeyboardAvoidingView |
| 图片模糊 | 未适配DPR | 使用@2x/@3x图片 |
